"""
Views for expense management dashboard with analytics.
"""
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from django.http import JsonResponse
from django.db.models import Sum, Q
from django.core.paginator import Paginator
from datetime import datetime
from decimal import Decimal
from dateutil.relativedelta import relativedelta
from .models import Budget, Expense
from .forms import BudgetForm, ExpenseForm, ExpenseFilterForm
from .services import ExpenseAnalytics


class DashboardView(LoginRequiredMixin, View):
    """
    Enhanced dashboard with analytics, charts, and AI insights.
    """
    def get(self, request):
        from expenses.services import UnifiedDataService
        
        # Get selected month from query parameter, default to current month
        selected_month = request.GET.get('month', datetime.now().strftime('%Y-%m'))
        
        # Validate month format
        try:
            selected_date = datetime.strptime(selected_month, '%Y-%m')
        except ValueError:
            selected_month = datetime.now().strftime('%Y-%m')
            selected_date = datetime.now()
        
        # Create data service with selected month
        data_service = UnifiedDataService(request.user, selected_month=selected_month)
        summary = data_service.get_consistent_summary()
        kpi_data = data_service.get_kpi_data()
        
        # Get AI prediction and insights (context-aware based on selected month)
        from ai_engine.forecast import predict_next_day_expense, predict_next_month_expense, get_expense_forecast_chart
        from ai_engine.insights import generate_user_insights
        import json
        
        current_date = datetime.now()
        is_current_month = selected_month == current_date.strftime('%Y-%m')
        is_future_month = selected_date > current_date
        is_past_month = selected_date < current_date.replace(day=1)
        
        # Only show AI predictions for current and future months
        if is_current_month:
            ai_prediction = predict_next_day_expense(request.user)
            ai_monthly_forecast = predict_next_month_expense(request.user)
            ai_forecast_chart = get_expense_forecast_chart(request.user, months_ahead=4)
            ai_insights = generate_user_insights(request.user)
        elif is_future_month:
            # For future months, show forecasting data
            ai_prediction = {'message': f'No prediction available for future month {selected_date.strftime("%B %Y")}'}
            ai_monthly_forecast = predict_next_month_expense(request.user)
            ai_forecast_chart = get_expense_forecast_chart(request.user, months_ahead=4)
            ai_insights = generate_user_insights(request.user)
        else:
            # For past months, show historical analysis instead of predictions
            ai_prediction = {'message': f'Historical data for {selected_date.strftime("%B %Y")}'}
            ai_monthly_forecast = {'message': f'Historical month - actual data available'}
            ai_forecast_chart = get_expense_forecast_chart(request.user, months_ahead=4)
            ai_insights = generate_user_insights(request.user)
        
        # Serialize chart data as JSON for JavaScript
        if ai_forecast_chart and ai_forecast_chart.get('chart_data'):
            ai_forecast_chart['chart_data_json'] = json.dumps(ai_forecast_chart['chart_data'])
        
        # Get budget form for selected month
        budget = Budget.objects.filter(
            user=request.user,
            month=selected_month
        ).first()
        budget_form = BudgetForm(instance=budget)
        
        # Get recent expenses for selected month
        recent_expenses = Expense.objects.filter(
            user=request.user,
            date__year=selected_date.year,
            date__month=selected_date.month
        ).order_by('-date', '-created_at')[:5]
        
        # Generate month choices for dropdown
        month_choices = []
        current_date = datetime.now()
        
        # Add previous 12 months, current month, and next 12 months
        for i in range(12, -13, -1):  # From 12 months ago to 12 months ahead
            target_date = current_date - relativedelta(months=i)
            month_str = target_date.strftime('%Y-%m')
            month_display = target_date.strftime('%B %Y')
            month_choices.append((month_str, month_display))
        
        # Calculate savings ratio compared to previous month
        from django.db.models.functions import TruncMonth
        
        selected_month_date = selected_date.date().replace(day=1)
        previous_month_date = selected_month_date - relativedelta(months=1)
        
        # Get selected month expenses
        selected_month_expenses = Expense.objects.filter(
            user=request.user,
            date__gte=selected_month_date,
            date__lt=selected_month_date + relativedelta(months=1)
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Get previous month expenses
        previous_month_expenses = Expense.objects.filter(
            user=request.user,
            date__gte=previous_month_date,
            date__lt=selected_month_date
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Calculate savings ratio
        savings_data = {
            'current_month_total': float(selected_month_expenses),
            'previous_month_total': float(previous_month_expenses),
            'savings_amount': float(previous_month_expenses - selected_month_expenses),
            'savings_percentage': 0,
            'is_saving': False,
            'trend': 'neutral'
        }
        
        if previous_month_expenses > 0:
            savings_data['savings_percentage'] = ((previous_month_expenses - selected_month_expenses) / previous_month_expenses) * 100
            savings_data['is_saving'] = selected_month_expenses < previous_month_expenses
            
            if savings_data['savings_percentage'] > 5:
                savings_data['trend'] = 'positive'
            elif savings_data['savings_percentage'] < -5:
                savings_data['trend'] = 'negative'
            else:
                savings_data['trend'] = 'neutral'
        
        context = {
            'summary': summary,
            'kpi_data': kpi_data,
            'budget_form': budget_form,
            'recent_expenses': recent_expenses,
            'selected_month': selected_month,
            'selected_month_display': selected_date.strftime('%B %Y'),
            'month_choices': month_choices,
            'ai_prediction': ai_prediction,
            'ai_monthly_forecast': ai_monthly_forecast,
            'ai_forecast_chart': ai_forecast_chart,
            'ai_insights': ai_insights,
            'savings_data': savings_data,
            'is_current_month': is_current_month,
            'is_future_month': is_future_month,
            'is_past_month': is_past_month,
        }
        
        return render(request, 'expenses/dashboard_modern.html', context)


class AddExpenseView(LoginRequiredMixin, View):
    """
    Add new expense.
    """
    def get(self, request):
        form = ExpenseForm()
        return render(request, 'expenses/add_expense_modern.html', {'form': form})
    
    def post(self, request):
        form = ExpenseForm(request.POST)
        if form.is_valid():
            expense = form.save(commit=False)
            expense.user = request.user
            expense.save()
            messages.success(request, f'Expense of ₹{expense.amount} added successfully!')
            return redirect('expenses:dashboard')
        return render(request, 'expenses/add_expense_modern.html', {'form': form})


class EditExpenseView(LoginRequiredMixin, View):
    """
    Edit existing expense.
    """
    def get(self, request, expense_id):
        expense = get_object_or_404(Expense, id=expense_id, user=request.user)
        form = ExpenseForm(instance=expense)
        return render(request, 'expenses/edit_expense.html', {
            'form': form,
            'expense': expense
        })
    
    def post(self, request, expense_id):
        expense = get_object_or_404(Expense, id=expense_id, user=request.user)
        form = ExpenseForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
            messages.success(request, 'Expense updated successfully!')
            return redirect('expenses:list_expenses')
        return render(request, 'expenses/edit_expense.html', {
            'form': form,
            'expense': expense
        })


class DeleteExpenseView(LoginRequiredMixin, View):
    """
    Delete an expense.
    """
    def post(self, request, expense_id):
        expense = get_object_or_404(Expense, id=expense_id, user=request.user)
        amount = expense.amount
        expense.delete()
        messages.success(request, f'Expense of ₹{amount} deleted successfully!')
        
        # Redirect to referring page or dashboard
        next_url = request.POST.get('next', 'expenses:dashboard')
        return redirect(next_url)


class ListExpensesView(LoginRequiredMixin, View):
    """
    List all expenses with filtering and pagination.
    """
    def get(self, request):
        # Get selected month from URL parameter for pre-filtering
        selected_month = request.GET.get('month')
        
        # Get all user expenses
        expenses = Expense.objects.filter(user=request.user)
        
        # Pre-populate filter form with month if provided
        initial_data = {}
        if selected_month:
            initial_data['month'] = selected_month
        
        # Apply filters
        filter_form = ExpenseFilterForm(request.GET or initial_data)
        if filter_form.is_valid():
            category = filter_form.cleaned_data.get('category')
            month = filter_form.cleaned_data.get('month')
            search = filter_form.cleaned_data.get('search')
            
            if category:
                expenses = expenses.filter(category=category)
            
            if month:
                year, month_num = month.split('-')
                expenses = expenses.filter(date__year=year, date__month=month_num)
            
            if search:
                expenses = expenses.filter(
                    Q(description__icontains=search) | Q(category__icontains=search)
                )
        
        # Pagination
        paginator = Paginator(expenses, 15)  # 15 expenses per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        # Calculate total
        total = expenses.aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        context = {
            'page_obj': page_obj,
            'filter_form': filter_form,
            'total': total,
            'count': expenses.count(),
            'average': total / expenses.count() if expenses.count() > 0 else 0,
            'selected_month': selected_month,
        }
        
        return render(request, 'expenses/list_expenses_modern.html', context)


class AnalyticsView(LoginRequiredMixin, View):
    """
    Detailed analytics page with AI forecasting.
    """
    def get(self, request):
        from expenses.services import UnifiedDataService
        from ai_engine.forecast import predict_next_month_expense, get_expense_forecast_chart, get_spending_analysis
        import json
        
        # Get selected month from query parameter, default to current month
        selected_month = request.GET.get('month', datetime.now().strftime('%Y-%m'))
        
        # Validate month format
        try:
            selected_date = datetime.strptime(selected_month, '%Y-%m')
        except ValueError:
            selected_month = datetime.now().strftime('%Y-%m')
            selected_date = datetime.now()
        
        # Create data service with selected month
        data_service = UnifiedDataService(request.user, selected_month=selected_month)
        summary = data_service.get_consistent_summary()
        kpi_data = data_service.get_kpi_data()
        chart_data = data_service.get_chart_data()
        
        # AI Forecasting data (context-aware for selected month)
        current_date_now = datetime.now()
        is_current_month = selected_month == current_date_now.strftime('%Y-%m')
        is_future_month = selected_date > current_date_now
        is_past_month = selected_date < current_date_now.replace(day=1)
        
        # Context-aware AI predictions
        if is_current_month:
            ai_monthly_forecast = predict_next_month_expense(request.user)
            ai_forecast_chart = get_expense_forecast_chart(request.user, months_ahead=6)
            spending_analysis = get_spending_analysis(request.user)
        elif is_future_month:
            ai_monthly_forecast = predict_next_month_expense(request.user)
            ai_forecast_chart = get_expense_forecast_chart(request.user, months_ahead=6)
            spending_analysis = {'message': f'Future month analysis for {selected_date.strftime("%B %Y")}'}
        else:
            ai_monthly_forecast = {'message': f'Historical data for {selected_date.strftime("%B %Y")}'}
            ai_forecast_chart = get_expense_forecast_chart(request.user, months_ahead=6)
            spending_analysis = {'message': f'Historical analysis for {selected_date.strftime("%B %Y")}'}
        
        # Serialize chart data as JSON for JavaScript
        if ai_forecast_chart and ai_forecast_chart.get('chart_data'):
            ai_forecast_chart['chart_data_json'] = json.dumps(ai_forecast_chart['chart_data'])
        
        # Generate month choices for dropdown
        month_choices = []
        current_date = datetime.now()
        
        # Add previous 12 months, current month, and next 12 months
        for i in range(12, -13, -1):  # From 12 months ago to 12 months ahead
            target_date = current_date - relativedelta(months=i)
            month_str = target_date.strftime('%Y-%m')
            month_display = target_date.strftime('%B %Y')
            month_choices.append((month_str, month_display))
        
        # Serialize other chart data for JavaScript
        def serialize_chart_data(data):
            """Convert Decimal and datetime objects to JSON-serializable formats"""
            if isinstance(data, list):
                return [serialize_chart_data(item) for item in data]
            elif isinstance(data, dict):
                result = {}
                for key, value in data.items():
                    if key == 'month' and hasattr(value, 'strftime'):
                        result[key] = value.strftime('%Y-%m')
                    elif hasattr(value, '__float__'):  # Decimal
                        result[key] = float(value)
                    else:
                        result[key] = serialize_chart_data(value)
                return result
            else:
                return data
        
        category_breakdown_serialized = serialize_chart_data(chart_data.get('category_breakdown', []))
        monthly_totals_serialized = serialize_chart_data(chart_data.get('monthly_totals', []))
        
        category_breakdown_json = json.dumps(category_breakdown_serialized)
        monthly_totals_json = json.dumps(monthly_totals_serialized)
        
        # Generate trend data (daily expenses for selected month)
        from datetime import timedelta
        from django.db.models import Sum
        from django.db.models.functions import TruncDate
        from expenses.models import Expense
        
        # Get start and end dates for selected month
        start_date = selected_date.date().replace(day=1)
        if selected_date.month == 12:
            end_date = selected_date.date().replace(year=selected_date.year + 1, month=1, day=1) - timedelta(days=1)
        else:
            end_date = selected_date.date().replace(month=selected_date.month + 1, day=1) - timedelta(days=1)
        
        daily_expenses = Expense.objects.filter(
            user=request.user,
            date__gte=start_date,
            date__lte=end_date
        ).annotate(
            day=TruncDate('date')
        ).values('day').annotate(
            total=Sum('amount')
        ).order_by('day')
        
        # Create trend data for selected month
        trend_data = []
        current_date = start_date
        while current_date <= end_date:
            day_expense = next((item for item in daily_expenses if item['day'] == current_date), None)
            trend_data.append({
                'date': current_date.strftime('%Y-%m-%d'),
                'total': float(day_expense['total']) if day_expense else 0
            })
            current_date += timedelta(days=1)
        
        trend_data_json = json.dumps(trend_data)
        
        # Calculate savings ratio compared to previous month
        from django.db.models.functions import TruncMonth
        
        selected_month_date = selected_date.date().replace(day=1)
        previous_month_date = selected_month_date - relativedelta(months=1)
        
        # Get selected month expenses
        selected_month_expenses = Expense.objects.filter(
            user=request.user,
            date__gte=selected_month_date,
            date__lt=selected_month_date + relativedelta(months=1)
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Get previous month expenses
        previous_month_expenses = Expense.objects.filter(
            user=request.user,
            date__gte=previous_month_date,
            date__lt=selected_month_date
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Calculate savings ratio
        savings_data = {
            'current_month_total': float(selected_month_expenses),
            'previous_month_total': float(previous_month_expenses),
            'savings_amount': float(previous_month_expenses - selected_month_expenses),
            'savings_percentage': 0,
            'is_saving': False,
            'trend': 'neutral'
        }
        
        if previous_month_expenses > 0:
            savings_data['savings_percentage'] = ((previous_month_expenses - selected_month_expenses) / previous_month_expenses) * 100
            savings_data['is_saving'] = selected_month_expenses < previous_month_expenses
            
            if savings_data['savings_percentage'] > 5:
                savings_data['trend'] = 'positive'
            elif savings_data['savings_percentage'] < -5:
                savings_data['trend'] = 'negative'
            else:
                savings_data['trend'] = 'neutral'
        
        context = {
            'summary': summary,
            'kpi_data': kpi_data,
            'chart_data': chart_data,
            'budget_status': summary['budget_status'],
            'total_expenses': summary['total_expenses'],
            'transaction_count': summary['transaction_count'],
            'average_transaction': summary['average_transaction'],
            'category_breakdown': chart_data['category_breakdown'],
            'monthly_totals': chart_data['monthly_totals'],
            'ai_monthly_forecast': ai_monthly_forecast,
            'ai_forecast_chart': ai_forecast_chart,
            'spending_analysis': spending_analysis,
            'category_breakdown_json': category_breakdown_json,
            'monthly_totals_json': monthly_totals_json,
            'trend_data_json': trend_data_json,
            'savings_data': savings_data,
            'selected_month': selected_month,
            'selected_month_display': selected_date.strftime('%B %Y'),
            'month_choices': month_choices,
            'is_current_month': is_current_month,
            'is_future_month': is_future_month,
            'is_past_month': is_past_month,
        }
        
        return render(request, 'expenses/analytics_modern.html', context)


class SetBudgetView(LoginRequiredMixin, View):
    """
    Set or update monthly budget.
    """
    def post(self, request):
        form = BudgetForm(request.POST)
        
        if form.is_valid():
            month = form.cleaned_data['month']
            amount = form.cleaned_data['amount']
            
            # Update or create budget
            budget, created = Budget.objects.update_or_create(
                user=request.user,
                month=month,
                defaults={'amount': amount}
            )
            
            if created:
                messages.success(request, f'Budget set successfully for {month}!')
            else:
                messages.success(request, f'Budget updated successfully for {month}!')
        else:
            messages.error(request, 'Invalid budget data. Please try again.')
        
        return redirect('expenses:dashboard')


class BudgetManagementView(LoginRequiredMixin, View):
    """
    Comprehensive budget management page.
    """
    def get(self, request):
        # Get all user budgets
        budgets = Budget.objects.filter(user=request.user).order_by('-month')
        
        # Get budget form
        budget_form = BudgetForm()
        
        # Generate budget overview for last 12 months
        budget_overview = []
        current_date = datetime.now()
        
        for i in range(12):
            if current_date.month - i <= 0:
                month_date = datetime(current_date.year - 1, 12 + (current_date.month - i), 1)
            else:
                month_date = datetime(current_date.year, current_date.month - i, 1)
            
            month_str = month_date.strftime('%Y-%m')
            month_display = month_date.strftime('%B %Y')
            
            # Get budget for this month
            budget = budgets.filter(month=month_str).first()
            
            # Get expenses for this month
            expenses = Expense.objects.filter(
                user=request.user,
                date__year=month_date.year,
                date__month=month_date.month
            ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
            
            # Calculate savings and usage
            budget_amount = budget.amount if budget else Decimal('0.00')
            savings = budget_amount - expenses if budget_amount > 0 else Decimal('0.00')
            usage_percentage = (expenses / budget_amount * 100) if budget_amount > 0 else 0
            
            budget_overview.append({
                'month': month_str,
                'month_display': month_display,
                'budget': budget,
                'budget_amount': budget_amount,
                'expenses': expenses,
                'savings': savings,
                'usage_percentage': min(100, usage_percentage),
                'is_over_budget': expenses > budget_amount if budget_amount > 0 else False,
                'has_budget': budget is not None
            })
        
        context = {
            'budgets': budgets,
            'budget_form': budget_form,
            'budget_overview': budget_overview,
        }
        
        return render(request, 'expenses/budget_management.html', context)
    
    def post(self, request):
        # Handle budget creation/update
        form = BudgetForm(request.POST)
        
        if form.is_valid():
            month = form.cleaned_data['month']
            amount = form.cleaned_data['amount']
            
            # Update or create budget
            budget, created = Budget.objects.update_or_create(
                user=request.user,
                month=month,
                defaults={'amount': amount}
            )
            
            action = "set" if created else "updated"
            month_display = datetime.strptime(month, '%Y-%m').strftime('%B %Y')
            messages.success(request, f'Budget {action} successfully for {month_display}!')
        else:
            messages.error(request, 'Invalid budget data. Please try again.')
        
        return redirect('expenses:budget_management')


# API Views for Chart Data

class CategoryChartDataView(LoginRequiredMixin, View):
    """
    API endpoint for category distribution chart.
    """
    def get(self, request):
        analytics = ExpenseAnalytics(request.user)
        breakdown = analytics.get_category_breakdown()
        
        labels = [item['category'] for item in breakdown]
        data = [float(item['total']) for item in breakdown]
        
        colors = [
            '#4f46e5', '#10b981', '#f59e0b', '#ef4444', '#8b5cf6',
            '#ec4899', '#06b6d4', '#84cc16', '#f97316', '#6366f1'
        ]
        
        return JsonResponse({
            'labels': labels,
            'data': data,
            'colors': colors[:len(labels)]
        })


class MonthlyChartDataView(LoginRequiredMixin, View):
    """
    API endpoint for monthly expenses chart.
    """
    def get(self, request):
        analytics = ExpenseAnalytics(request.user)
        monthly_data = analytics.get_monthly_totals(6)
        
        labels = [item['month'].strftime('%b %Y') for item in monthly_data]
        data = [float(item['total']) for item in monthly_data]
        
        return JsonResponse({
            'labels': labels,
            'data': data
        })


class TrendChartDataView(LoginRequiredMixin, View):
    """
    API endpoint for spending trend chart.
    """
    def get(self, request):
        analytics = ExpenseAnalytics(request.user)
        trend_data = analytics.get_spending_trend(30)
        
        labels = [item['date'].strftime('%b %d') for item in trend_data]
        data = [float(item['total']) for item in trend_data]
        
        return JsonResponse({
            'labels': labels,
            'data': data
        })
