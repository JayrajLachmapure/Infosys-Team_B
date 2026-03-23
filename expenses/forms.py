"""
Forms for budget and expense management.
"""
from django import forms
from .models import Budget, Expense
from datetime import datetime


class BudgetForm(forms.ModelForm):
    """
    Form for setting monthly budget.
    """
    month = forms.CharField(
        widget=forms.Select(attrs={
            'class': 'form-input',
        }),
        help_text="Select month"
    )

    class Meta:
        model = Budget
        fields = ['month', 'amount']
        widgets = {
            'amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter budget amount in ₹',
                'step': '0.01',
                'min': '0.01'
            }),
        }
        labels = {
            'amount': 'Budget Amount (₹)'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate month choices for previous 12 months, current month, and next 12 months
        months = []
        current_date = datetime.now()
        
        # Add previous 12 months
        for i in range(12, 0, -1):
            if current_date.month - i <= 0:
                month_date = datetime(current_date.year - 1, 12 + (current_date.month - i), 1)
            else:
                month_date = datetime(current_date.year, current_date.month - i, 1)
            month_str = month_date.strftime('%Y-%m')
            month_display = month_date.strftime('%B %Y')
            months.append((month_str, month_display))
        
        # Add current and next 12 months
        for i in range(13):  # 0 to 12 (current + next 12)
            if current_date.month + i > 12:
                year_offset = (current_date.month + i - 1) // 12
                month_num = ((current_date.month + i - 1) % 12) + 1
                month_date = datetime(current_date.year + year_offset, month_num, 1)
            else:
                month_date = datetime(current_date.year, current_date.month + i, 1)
            month_str = month_date.strftime('%Y-%m')
            month_display = month_date.strftime('%B %Y')
            months.append((month_str, month_display))
        
        # Set current month as default if creating new budget
        if not self.instance.pk:
            current_month_str = current_date.strftime('%Y-%m')
            self.fields['month'].initial = current_month_str
        
        self.fields['month'].widget = forms.Select(
            choices=months,
            attrs={'class': 'form-input'}
        )


class ExpenseForm(forms.ModelForm):
    """
    Form for adding and editing expenses.
    """
    class Meta:
        model = Expense
        fields = ['date', 'amount', 'category', 'description']
        widgets = {
            'date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter amount in ₹',
                'step': '0.01',
                'min': '0.01'
            }),
            'category': forms.Select(attrs={
                'class': 'form-input',
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-input',
                'placeholder': 'Add a description (optional)',
                'rows': 3
            }),
        }
        labels = {
            'description': 'Description (Optional)',
            'amount': 'Amount (₹)'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set default date to today
        if not self.instance.pk:
            self.fields['date'].initial = datetime.now().date()


class ExpenseFilterForm(forms.Form):
    """
    Form for filtering expenses.
    """
    category = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={'class': 'form-input'}),
        label='Category'
    )
    month = forms.ChoiceField(
        required=False,
        widget=forms.Select(attrs={'class': 'form-input'}),
        label='Month'
    )
    search = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Search description...'
        }),
        label='Search'
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # Category choices
        categories = [('', 'All Categories')] + list(Expense.CATEGORY_CHOICES)
        self.fields['category'].choices = categories
        
        # Month choices (last 12 months)
        months = [('', 'All Months')]
        current_date = datetime.now()
        for i in range(12):
            month_date = datetime(current_date.year, current_date.month, 1)
            if current_date.month - i <= 0:
                month_date = datetime(current_date.year - 1, 12 + (current_date.month - i), 1)
            else:
                month_date = datetime(current_date.year, current_date.month - i, 1)
            month_str = month_date.strftime('%Y-%m')
            month_display = month_date.strftime('%B %Y')
            months.append((month_str, month_display))
        
        self.fields['month'].choices = months
