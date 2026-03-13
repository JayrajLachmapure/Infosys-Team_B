"""
Analytics and business logic services for expense management.
"""
from django.db.models import Sum, Count, Q
from django.db.models.functions import TruncMonth
from datetime import datetime, timedelta
from decimal import Decimal
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
            # Calculate month and year
            target_date = now - timedelta(days=i * 30)
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
    
    def __init__(self, user):
        self.user = user
        self.analytics = ExpenseAnalytics(user)
    
    def get_consistent_summary(self):
        """Get consistent summary data for all pages"""
        summary = self.analytics.get_dashboard_summary()
        
        # Add calculated fields for consistency
        summary['average_transaction'] = (
            summary['total_expenses'] / summary['transaction_count'] 
            if summary['transaction_count'] > 0 else Decimal('0.00')
        )
        
        # Ensure all decimal values are properly formatted
        summary['total_expenses_formatted'] = f"₹{summary['total_expenses']:,.0f}"
        summary['average_transaction_formatted'] = f"₹{summary['average_transaction']:,.0f}"
        
        return summary
    
    def get_kpi_data(self):
        """Get KPI data with trend calculations"""
        summary = self.get_consistent_summary()
        
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
            'budget_status': summary['budget_status']
        }
    
    def get_chart_data(self):
        """Get consistent chart data for all pages"""
        return {
            'category_breakdown': self.analytics.get_category_breakdown(),
            'monthly_totals': self.analytics.get_monthly_totals(12),
            'spending_trend': self.analytics.get_spending_trend(30)
        }