"""
AI Insights Generator
Generates intelligent financial insights and recommendations.
"""
from datetime import datetime, timedelta
from decimal import Decimal
from django.db.models import Sum, Avg, Count
from expenses.models import Expense, Budget
from expenses.services import ExpenseAnalytics


class FinancialInsightsEngine:
    """
    Generate AI-powered financial insights for users.
    """
    
    def __init__(self, user):
        self.user = user
        self.analytics = ExpenseAnalytics(user)
    
    def detect_overspending(self, threshold_percentage=20):
        """
        Detect if current month spending is significantly higher than average.
        
        Args:
            threshold_percentage: Percentage above average to trigger alert
        
        Returns:
            dict: Overspending alert information
        """
        current_month_total = self.analytics.get_current_month_total()
        
        # Get average of last 3-6 months (excluding current)
        now = datetime.now()
        six_months_ago = now - timedelta(days=180)
        
        historical_expenses = Expense.objects.filter(
            user=self.user,
            date__gte=six_months_ago,
            date__lt=datetime(now.year, now.month, 1)  # Exclude current month
        )
        
        if not historical_expenses.exists():
            return {
                'is_overspending': False,
                'message': 'Not enough historical data to compare.',
                'percentage_above_average': 0,
                'current_spending': float(current_month_total),
                'average_spending': 0
            }
        
        # Calculate monthly average
        from django.db.models.functions import TruncMonth
        
        months_data = historical_expenses.annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            total=Sum('amount')
        ).order_by('month')
        
        if not months_data:
            return {
                'is_overspending': False,
                'message': 'Not enough data.',
                'percentage_above_average': 0,
                'current_spending': float(current_month_total),
                'average_spending': 0
            }
        
        average_spending = sum(m['total'] for m in months_data) / len(months_data)
        
        if average_spending == 0:
            return {
                'is_overspending': False,
                'message': 'No historical spending data.',
                'percentage_above_average': 0,
                'current_spending': float(current_month_total),
                'average_spending': 0
            }
        
        percentage_diff = ((current_month_total - average_spending) / average_spending) * 100
        
        is_overspending = percentage_diff > threshold_percentage
        
        if is_overspending:
            message = f"⚠️ Your spending this month is {abs(percentage_diff):.1f}% higher than your average."
        elif percentage_diff < -threshold_percentage:
            message = f"✅ Great job! Your spending is {abs(percentage_diff):.1f}% lower than average."
        else:
            message = "✓ Your spending is within normal range."
        
        return {
            'is_overspending': is_overspending,
            'message': message,
            'percentage_above_average': round(percentage_diff, 1),
            'current_spending': float(current_month_total),
            'average_spending': float(average_spending)
        }
    
    def get_highest_spending_category(self):
        """
        Identify the category with highest spending this month.
        """
        breakdown = self.analytics.get_category_breakdown()
        
        if not breakdown:
            return {
                'category': 'None',
                'amount': 0,
                'message': 'No expenses recorded this month.'
            }
        
        highest = breakdown[0]
        
        return {
            'category': highest['category'],
            'amount': float(highest['total']),
            'count': highest['count'],
            'message': f"You spent the most on {highest['category']} this month (₹{highest['total']:.2f})."
        }
    
    def calculate_spending_change(self):
        """
        Calculate spending change compared to last month.
        """
        now = datetime.now()
        
        # Current month
        current_total = self.analytics.get_current_month_total()
        
        # Last month
        if now.month == 1:
            last_month = 12
            last_year = now.year - 1
        else:
            last_month = now.month - 1
            last_year = now.year
        
        last_month_total = Expense.objects.filter(
            user=self.user,
            date__year=last_year,
            date__month=last_month
        ).aggregate(total=Sum('amount'))['total'] or Decimal('0.00')
        
        if last_month_total == 0:
            return {
                'change_percentage': 0,
                'change_amount': 0,
                'direction': 'stable',
                'message': 'No data from last month to compare.'
            }
        
        change_amount = current_total - last_month_total
        change_percentage = (change_amount / last_month_total) * 100
        
        if change_percentage > 10:
            direction = 'increased'
            message = f"📈 Your expenses increased by {abs(change_percentage):.1f}% compared to last month."
        elif change_percentage < -10:
            direction = 'decreased'
            message = f"📉 Your expenses decreased by {abs(change_percentage):.1f}% compared to last month."
        else:
            direction = 'stable'
            message = "➡️ Your spending is relatively stable compared to last month."
        
        return {
            'change_percentage': round(change_percentage, 1),
            'change_amount': float(change_amount),
            'direction': direction,
            'message': message,
            'current_month': float(current_total),
            'last_month': float(last_month_total)
        }
    
    def generate_savings_advice(self):
        """
        Generate personalized savings recommendations.
        """
        breakdown = self.analytics.get_category_breakdown()
        budget_status = self.analytics.get_budget_status()
        
        advice = []
        
        # Check budget status
        if budget_status['budget'] > 0:
            if budget_status['remaining'] < 0:
                advice.append({
                    'type': 'urgent',
                    'icon': '🚨',
                    'message': f"You've exceeded your budget by ₹{abs(budget_status['remaining']):.2f}. Consider cutting non-essential expenses."
                })
            elif budget_status['percentage'] > 80:
                advice.append({
                    'type': 'warning',
                    'icon': '⚠️',
                    'message': f"You've used {budget_status['percentage']:.1f}% of your budget. Be cautious with remaining expenses."
                })
        
        # Analyze categories
        if breakdown:
            # Check for high discretionary spending
            discretionary = ['Entertainment', 'Shopping', 'Food', 'Travel']
            discretionary_total = sum(
                item['total'] for item in breakdown 
                if item['category'] in discretionary
            )
            
            total_spending = sum(item['total'] for item in breakdown)
            
            if total_spending > 0:
                discretionary_percentage = (discretionary_total / total_spending) * 100
                
                if discretionary_percentage > 40:
                    advice.append({
                        'type': 'suggestion',
                        'icon': '💡',
                        'message': f"Discretionary spending is {discretionary_percentage:.1f}% of your total. Consider reducing entertainment or shopping expenses."
                    })
            
            # Suggest reducing highest category if it's discretionary
            highest = breakdown[0]
            if highest['category'] in discretionary:
                advice.append({
                    'type': 'suggestion',
                    'icon': '💰',
                    'message': f"Consider reducing {highest['category']} expenses to save more."
                })
        
        # General advice if no specific issues
        if not advice:
            advice.append({
                'type': 'positive',
                'icon': '✅',
                'message': "Your spending looks healthy! Keep tracking to maintain good financial habits."
            })
        
        return advice
    
    def generate_user_insights(self):
        """
        Generate comprehensive financial insights for the user.
        
        Returns:
            dict: Complete insights package
        """
        return {
            'overspending_alert': self.detect_overspending(),
            'highest_category': self.get_highest_spending_category(),
            'spending_change': self.calculate_spending_change(),
            'savings_advice': self.generate_savings_advice(),
            'budget_status': self.analytics.get_budget_status(),
            'transaction_count': self.analytics.get_transaction_count()
        }


def generate_user_insights(user):
    """
    Convenience function to generate insights for a user.
    
    Args:
        user: Django User object
    
    Returns:
        dict: Financial insights
    """
    engine = FinancialInsightsEngine(user)
    return engine.generate_user_insights()
