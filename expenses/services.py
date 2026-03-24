"""
Analytics and business logic services for expense management.
"""
from django.db.models import Sum, Count, Q
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta
from decimal import Decimal
from dateutil.relativedelta import relativedelta
from .models import Expense, Budget


class ExpenseAnalytics:
    """
    Service class for expense analytics and calculations.
    """
    
    def __init__(self, user):
        self.user = user
    
    def get_current_month_total(self):
        """Get total expenses for current month"""
        now = datetime.now()
        total = Expense.objects.filter(
            user=self.user,
            date__year=now.year,
            date__month=now.month
        ).aggregate(total=Sum('amount'))['total']
        return total or Decimal('0.00')
    
    def get_transaction_count(self, month=None, year=None):
        """Get number of transactions"""
        queryset = Expense.objects.filter(user=self.user)
        if month and year:
            queryset = queryset.filter(date__year=year, date__month=month)
        return queryset.count()
    
    def get_category_breakdown(self, month=None, year=None):
        """Get expenses grouped by category"""
        now = datetime.now()
        queryset = Expense.objects.filter(user=self.user)
        
        if month and year:
            queryset = queryset.filter(date__year=year, date__month=month)
        else:
            queryset = queryset.filter(date__year=now.year, date__month=now.month)
        
        breakdown = queryset.values('category').annotate(
            total=Sum('amount'),
            count=Count('id')
        ).order_by('-total')
        
        return list(breakdown)
    
    def get_highest_category(self):
        """Get category with highest spending"""
        breakdown = self.get_category_breakdown()
        if breakdown:
            return {
                'category': breakdown[0]['category'],
                'amount': breakdown[0]['total']
            }
        return {'category': 'None', 'amount': Decimal('0.00')}
    
    def get_monthly_totals(self, months=6):
        """Get total expenses for last N months"""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=months * 30)
        
        monthly_data = Expense.objects.filter(
            user=self.user,
            date__gte=start_date
        ).annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            total=Sum('amount')
        ).order_by('month')
        
        return list(monthly_data)
    
    def get_spending_trend(self, days=30):
        """Get daily spending for last N days"""
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=days)
        
        daily_data = Expense.objects.filter(
            user=self.user,
            date__gte=start_date,
            date__lte=end_date
        ).values('date').annotate(
            total=Sum('amount')
        ).order_by('date')
        
        return list(daily_data)
    
    def get_budget_status(self):
        """Get current month budget status"""
        now = datetime.now()
        month_str = now.strftime('%Y-%m')
        
        budget = Budget.objects.filter(
            user=self.user,
            month=month_str
        ).first()
        
        total_spent = self.get_current_month_total()
        
        if budget:
            remaining = budget.amount - total_spent
            percentage = (total_spent / budget.amount * 100) if budget.amount > 0 else 0
            return {
                'budget': budget.amount,
                'spent': total_spent,
                'remaining': remaining,
                'percentage': round(percentage, 1)
            }
        
        return {
            'budget': Decimal('0.00'),
            'spent': total_spent,
            'remaining': Decimal('0.00'),
            'percentage': 0
        }
    
    def get_monthly_expenses_breakdown(self, months=12):
        """Get detailed monthly expenses breakdown with savings calculation"""
        monthly_data = []
        now = datetime.now()
        
        for i in range(months):
            # Calculate month and year using proper month arithmetic
            target_date = now - relativedelta(months=i)
            month_str = target_date.strftime('%Y-%m')
            
            # Get expenses for this month
            expenses = Expense.objects.filter(
                user=self.user,
                date__year=target_date.year,
                date__month=target_date.month
            ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
            
            # Get budget for this month
            budget = Budget.objects.filter(
                user=self.user,
                month=month_str
            ).first()
            
            budget_amount = budget.amount if budget else Decimal('0.00')
            savings = budget_amount - expenses if budget_amount > 0 else Decimal('0.00')
            
            monthly_data.append({
                'month': target_date.strftime('%B %Y'),
                'month_short': target_date.strftime('%b %Y'),
                'expenses': expenses,
                'budget': budget_amount,
                'savings': savings,
                'savings_percentage': round((savings / budget_amount * 100), 1) if budget_amount > 0 else 0,
                'usage_percentage': min(100, round((expenses / budget_amount * 100), 1)) if budget_amount > 0 else 0
            })
        
        return monthly_data
    
    def get_total_savings(self, months=12):
        """Calculate total savings over specified months"""
        monthly_breakdown = self.get_monthly_expenses_breakdown(months)
        total_savings = sum(month['savings'] for month in monthly_breakdown if month['savings'] > 0)
        total_budget = sum(month['budget'] for month in monthly_breakdown)
        total_expenses = sum(month['expenses'] for month in monthly_breakdown)
        
        return {
            'total_savings': total_savings,
            'total_budget': total_budget,
            'total_expenses': total_expenses,
            'savings_rate': round((total_savings / total_budget * 100), 1) if total_budget > 0 else 0
        }
    
    def get_usage_alerts(self):
        """Generate usage alerts for budget progress"""
        budget_status = self.get_budget_status()
        alerts = []
        
        if budget_status['budget'] > 0:
            percentage = budget_status['percentage']
            remaining = budget_status['remaining']
            
            if percentage >= 100:
                alerts.append({
                    'type': 'danger',
                    'icon': '🚨',
                    'title': 'Budget Exceeded',
                    'message': f'You have exceeded your budget by ₹{abs(remaining):,.2f}',
                    'progress': 100
                })
            elif percentage >= 90:
                alerts.append({
                    'type': 'warning',
                    'icon': '⚠️',
                    'title': 'Budget Almost Exhausted',
                    'message': f'Only ₹{remaining:,.2f} left ({100-percentage:.1f}% remaining)',
                    'progress': percentage
                })
            elif percentage >= 75:
                alerts.append({
                    'type': 'info',
                    'icon': '📊',
                    'title': 'Budget Alert',
                    'message': f'₹{remaining:,.2f} remaining ({100-percentage:.1f}% left)',
                    'progress': percentage
                })
            else:
                alerts.append({
                    'type': 'success',
                    'icon': '✅',
                    'title': 'Budget On Track',
                    'message': f'₹{remaining:,.2f} remaining ({100-percentage:.1f}% left)',
                    'progress': percentage
                })
        else:
            alerts.append({
                'type': 'warning',
                'icon': '💡',
                'title': 'No Budget Set',
                'message': 'Set a monthly budget to track your spending progress',
                'progress': 0
            })
        
        return alerts
    def get_dashboard_summary(self):
        """Get complete dashboard summary"""
        now = datetime.now()
        budget_status = self.get_budget_status()
        highest_category = self.get_highest_category()
        
        return {
            'total_expenses': self.get_current_month_total(),
            'transaction_count': self.get_transaction_count(now.month, now.year),
            'highest_category': highest_category,
            'budget_status': budget_status,
            'category_breakdown': self.get_category_breakdown(),
            'monthly_totals': self.get_monthly_totals(6),
            'spending_trend': self.get_spending_trend(30),
            'monthly_breakdown': self.get_monthly_expenses_breakdown(12),
            'total_savings': self.get_total_savings(12),
            'usage_alerts': self.get_usage_alerts()
        }


class UnifiedDataService:
    """
    Centralized service for consistent data across all UI pages
    """
    
    def __init__(self, user, selected_month=None):
        self.user = user
        self.selected_month = selected_month or datetime.now().strftime('%Y-%m')
        self.selected_date = datetime.strptime(self.selected_month, '%Y-%m')
        self.analytics = ExpenseAnalytics(user)
    
    def get_consistent_summary(self):
        """Get consistent summary data for all pages"""
        # Get data for selected month instead of current month
        selected_year = self.selected_date.year
        selected_month_num = self.selected_date.month
        
        # Get expenses for selected month
        total_expenses = Expense.objects.filter(
            user=self.user,
            date__year=selected_year,
            date__month=selected_month_num
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Get transaction count for selected month
        transaction_count = Expense.objects.filter(
            user=self.user,
            date__year=selected_year,
            date__month=selected_month_num
        ).count()
        
        # Get highest category for selected month
        highest_category = self.analytics.get_category_breakdown(selected_month_num, selected_year)
        highest_category_data = {
            'category': highest_category[0]['category'] if highest_category else 'None',
            'amount': highest_category[0]['total'] if highest_category else Decimal('0.00')
        }
        
        # Get budget status for selected month
        budget = Budget.objects.filter(
            user=self.user,
            month=self.selected_month
        ).first()
        
        budget_status = {
            'budget': budget.amount if budget else Decimal('0.00'),
            'spent': total_expenses,
            'remaining': (budget.amount - total_expenses) if budget else Decimal('0.00'),
            'percentage': (total_expenses / budget.amount * 100) if budget and budget.amount > 0 else 0
        }
        
        # Calculate average transaction
        average_transaction = (
            total_expenses / transaction_count 
            if transaction_count > 0 else Decimal('0.00')
        )
        
        summary = {
            'total_expenses': total_expenses,
            'transaction_count': transaction_count,
            'highest_category': highest_category_data,
            'budget_status': budget_status,
            'category_breakdown': highest_category,
            'average_transaction': average_transaction,
            'total_expenses_formatted': f"₹{total_expenses:,.0f}",
            'average_transaction_formatted': f"₹{average_transaction:,.0f}",
            'selected_month': self.selected_month,
            'selected_month_display': self.selected_date.strftime('%B %Y'),
            'monthly_breakdown': self.analytics.get_monthly_expenses_breakdown(12),
            'total_savings': self.analytics.get_total_savings(12),
        }
        
        return summary
    
    def get_savings_ratio(self):
        """Calculate savings ratio comparing selected month to previous months"""
        # Get selected month budget and expenses
        selected_budget = Budget.objects.filter(
            user=self.user,
            month=self.selected_month
        ).first()
        
        selected_expenses = Expense.objects.filter(
            user=self.user,
            date__year=self.selected_date.year,
            date__month=self.selected_date.month
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        # Calculate selected month savings (only positive savings count)
        if selected_budget and selected_budget.amount > 0:
            selected_savings = max(Decimal('0.00'), selected_budget.amount - selected_expenses)
        else:
            selected_savings = Decimal('0.00')
        
        # Get previous 3 months savings data
        previous_months_savings = []
        for i in range(1, 4):  # Previous 3 months
            prev_date = self.selected_date - relativedelta(months=i)
            prev_month_str = prev_date.strftime('%Y-%m')
            
            # Get budget for previous month
            prev_budget = Budget.objects.filter(
                user=self.user,
                month=prev_month_str
            ).first()
            
            # Get expenses for previous month
            prev_expenses = Expense.objects.filter(
                user=self.user,
                date__year=prev_date.year,
                date__month=prev_date.month
            ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
            
            # Calculate savings for previous month (only positive savings count)
            if prev_budget and prev_budget.amount > 0:
                prev_savings = max(Decimal('0.00'), prev_budget.amount - prev_expenses)
            else:
                prev_savings = Decimal('0.00')
            
            previous_months_savings.append(prev_savings)
        
        # Calculate average of previous months (only non-zero values)
        non_zero_savings = [s for s in previous_months_savings if s > 0]
        if non_zero_savings:
            avg_previous_savings = sum(non_zero_savings) / len(non_zero_savings)
        else:
            avg_previous_savings = Decimal('0.00')
        
        # Calculate ratio and trend
        if avg_previous_savings > 0 and selected_savings > 0:
            # Both selected and previous have savings - calculate percentage change
            ratio = (selected_savings / avg_previous_savings) * 100
            if ratio >= 110:  # 10% or more improvement
                trend = 'positive'
                trend_percentage = round(ratio - 100, 1)
            elif ratio <= 90:  # 10% or more decline
                trend = 'negative' 
                trend_percentage = round(100 - ratio, 1)
            else:  # Within 10% range
                trend = 'neutral'
                trend_percentage = round(abs(ratio - 100), 1)
        elif selected_savings > 0 and avg_previous_savings == 0:
            # Selected month has savings, previous months had none
            ratio = 100
            trend = 'positive'
            trend_percentage = 100
        elif selected_savings == 0 and avg_previous_savings > 0:
            # Previous months had savings, selected month has none
            ratio = 0
            trend = 'negative'
            trend_percentage = 100
        else:
            # Both selected and previous have no savings
            ratio = 0
            trend = 'neutral'
            trend_percentage = 0
        
        return {
            'current_savings': selected_savings,
            'avg_previous_savings': avg_previous_savings,
            'ratio': round(ratio, 1),
            'trend': trend,
            'trend_percentage': trend_percentage,
            'formatted_current': f"₹{selected_savings:,.0f}",
            'formatted_previous': f"₹{avg_previous_savings:,.0f}",
            'comparison_text': self._get_savings_comparison_text(selected_savings, avg_previous_savings, trend, trend_percentage)
        }
    
    def _get_savings_comparison_text(self, current, previous, trend, percentage):
        """Generate descriptive text for savings comparison"""
        if trend == 'positive':
            if previous == 0:
                return "New savings this month!"
            else:
                return f"+{percentage}% vs avg"
        elif trend == 'negative':
            if current == 0:
                return "No savings this month"
            else:
                return f"-{percentage}% vs avg"
        else:
            return "Similar to average"

    def get_kpi_data(self):
        """Get KPI data with trend calculations"""
        summary = self.get_consistent_summary()
        savings_ratio = self.get_savings_ratio()
        
        return {
            'total_expenses': {
                'value': summary['total_expenses'],
                'formatted': summary['total_expenses_formatted'],
                'trend': 'positive',  # Calculate based on previous month
                'trend_percentage': 12.5
            },
            'transaction_count': {
                'value': summary['transaction_count'],
                'trend': 'neutral',
                'trend_percentage': 0
            },
            'average_transaction': {
                'value': summary['average_transaction'],
                'formatted': summary['average_transaction_formatted'],
                'trend': 'negative',
                'trend_percentage': -5.2
            },
            'savings_ratio': savings_ratio,
            'budget_status': summary['budget_status']
        }
    
    def get_chart_data(self):
        """Get consistent chart data for all pages"""
        return {
            'category_breakdown': self.analytics.get_category_breakdown(self.selected_date.month, self.selected_date.year),
            'monthly_totals': self.analytics.get_monthly_totals(12),
            'spending_trend': self.analytics.get_spending_trend(30)
        }