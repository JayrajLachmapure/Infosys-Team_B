"""
AI Expense Forecasting Module
Uses Linear Regression and Time Series forecasting to predict future expenses.
"""
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from datetime import datetime, timedelta
from decimal import Decimal
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDate
from expenses.models import Expense
from dateutil.relativedelta import relativedelta


class ExpenseForecastEngine:
    """
    Advanced Machine Learning engine for expense forecasting.
    """
    
    def __init__(self, user):
        self.user = user
        self.model = LinearRegression()
        self.scaler = StandardScaler()
        self.min_data_points = 3  # Minimum months of data required
    
    def get_monthly_historical_data(self, months=12):
        """
        Fetch and aggregate user's historical expense data by month.
        Returns DataFrame with month index and total expenses.
        """
        # Get expenses from last N months
        end_date = datetime.now()
        start_date = end_date - relativedelta(months=months)
        
        # Get monthly expenses
        monthly_expenses = Expense.objects.filter(
            user=self.user,
            date__gte=start_date
        ).annotate(
            month=TruncMonth('date')
        ).values('month').annotate(
            total=Sum('amount')
        ).order_by('month')
        
        if not monthly_expenses:
            return None
        
        # Convert to DataFrame
        df = pd.DataFrame(list(monthly_expenses))
        df['month_index'] = range(1, len(df) + 1)
        df['total'] = df['total'].apply(lambda x: float(x))
        df['month_name'] = df['month'].apply(lambda x: x.strftime('%b %Y'))
        
        return df
    
    def get_daily_historical_data(self, days=30):
        """
        Fetch and aggregate user's historical expense data by day.
        Returns DataFrame with day index and total expenses.
        """
        # Get expenses from last N days
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        # Get daily expenses
        daily_expenses = Expense.objects.filter(
            user=self.user,
            date__gte=start_date
        ).annotate(
            day=TruncDate('date')
        ).values('day').annotate(
            total=Sum('amount')
        ).order_by('day')
        
        if not daily_expenses:
            return None
        
        # Convert to DataFrame
        df = pd.DataFrame(list(daily_expenses))
        df['day_index'] = range(1, len(df) + 1)
        df['total'] = df['total'].apply(lambda x: float(x))
        
        return df
    
    def prepare_training_data(self, df, index_col='month_index'):
        """
        Prepare data for model training.
        Returns X (indices) and y (expense totals).
        """
        if df is None or len(df) < self.min_data_points:
            return None, None
        
        X = df[[index_col]].values
        y = df['total'].values
        
        return X, y
    
    def train_model(self, X, y):
        """
        Train Linear Regression model on historical data.
        """
        if X is None or y is None:
            return False
        
        try:
            # Fit the model
            self.model.fit(X, y)
            return True
        except Exception as e:
            print(f"Model training error: {e}")
            return False
    
    def predict_next_month_expense(self):
        """
        Predict expense for the next month based on historical monthly data.
        Returns comprehensive prediction with trend analysis.
        """
        # Get historical monthly data
        df = self.get_monthly_historical_data(months=12)
        
        if df is None or len(df) < self.min_data_points:
            return {
                'success': False,
                'message': f'Insufficient data. Need at least {self.min_data_points} months of expense history.',
                'predicted_amount': None,
                'confidence': None,
                'trend': None,
                'percentage_change': None
            }
        
        # Prepare training data
        X, y = self.prepare_training_data(df, 'month_index')
        
        # Train model
        if not self.train_model(X, y):
            return {
                'success': False,
                'message': 'Model training failed.',
                'predicted_amount': None,
                'confidence': None,
                'trend': None,
                'percentage_change': None
            }
        
        # Predict next month (month_index = last_month + 1)
        next_month_index = len(df) + 1
        predicted_amount = self.model.predict([[next_month_index]])[0]
        
        # Calculate confidence (R² score)
        confidence = self.model.score(X, y) * 100
        
        # Calculate percentage change from current month
        current_month_expense = df.iloc[-1]['total']
        percentage_change = ((predicted_amount - current_month_expense) / current_month_expense) * 100
        
        # Determine trend
        if percentage_change > 5:
            trend = 'increasing'
        elif percentage_change < -5:
            trend = 'decreasing'
        else:
            trend = 'stable'
        
        return {
            'success': True,
            'predicted_amount': round(predicted_amount, 2),
            'predicted_amount_formatted': f"₹{predicted_amount:,.0f}",
            'confidence': round(confidence, 1),
            'trend': trend,
            'percentage_change': round(percentage_change, 1),
            'current_month_expense': round(current_month_expense, 2),
            'data_points': len(df),
            'historical_data': df.to_dict('records')
        }
    
    def get_forecast_chart_data(self, months_ahead=4):
        """
        Generate forecast data for chart visualization.
        Returns historical + predicted data for charting.
        """
        # Get historical monthly data
        df = self.get_monthly_historical_data(months=6)
        
        if df is None or len(df) < self.min_data_points:
            return None
        
        # Prepare training data
        X, y = self.prepare_training_data(df, 'month_index')
        
        # Train model
        if not self.train_model(X, y):
            return None
        
        # Generate predictions for next months
        predictions = []
        last_month_index = len(df)
        current_date = datetime.now()
        
        for i in range(1, months_ahead + 1):
            month_index = last_month_index + i
            predicted = self.model.predict([[month_index]])[0]
            
            # Calculate future month name
            future_date = current_date + relativedelta(months=i)
            month_name = future_date.strftime('%b %Y')
            
            predictions.append({
                'month_name': month_name,
                'total': round(predicted, 2),
                'is_predicted': True
            })
        
        # Combine historical and predicted data
        historical = df[['month_name', 'total']].to_dict('records')
        for item in historical:
            item['is_predicted'] = False
        
        chart_data = historical + predictions
        
        return {
            'chart_data': chart_data,
            'historical_count': len(historical),
            'predicted_count': len(predictions)
        }
    
    def predict_next_day(self):
        """
        Predict expense for the next day based on daily data.
        """
        # Get historical daily data
        df = self.get_daily_historical_data(days=30)
        
        if df is None or len(df) < 7:  # Need at least a week of data
            return {
                'success': False,
                'message': 'Insufficient daily data. Need at least 7 days of expense history.',
                'predicted_amount': None,
                'confidence': None
            }
        
        # Prepare training data
        X, y = self.prepare_training_data(df, 'day_index')
        
        # Train model
        if not self.train_model(X, y):
            return {
                'success': False,
                'message': 'Model training failed.',
                'predicted_amount': None,
                'confidence': None
            }
        
        # Predict next day
        next_day_index = len(df) + 1
        predicted_amount = self.model.predict([[next_day_index]])[0]
        
        # Calculate confidence
        confidence = self.model.score(X, y) * 100
        
        return {
            'success': True,
            'predicted_amount': round(predicted_amount, 2),
            'predicted_amount_formatted': f"₹{predicted_amount:,.0f}",
            'confidence': round(confidence, 1),
            'data_points': len(df)
        }
    
    def get_spending_pattern_analysis(self):
        """
        Comprehensive spending pattern analysis.
        """
        df = self.get_monthly_historical_data(months=6)
        
        if df is None or len(df) < 2:
            return {
                'pattern': 'insufficient_data',
                'trend_strength': 0,
                'average_monthly': 0,
                'volatility': 'unknown'
            }
        
        # Calculate trend using linear regression slope
        X, y = self.prepare_training_data(df, 'month_index')
        self.train_model(X, y)
        
        slope = self.model.coef_[0]
        average_monthly = df['total'].mean()
        std_dev = df['total'].std()
        volatility_ratio = std_dev / average_monthly if average_monthly > 0 else 0
        
        # Determine pattern
        if slope > average_monthly * 0.05:  # Increasing by more than 5% per month
            pattern = 'increasing'
        elif slope < -average_monthly * 0.05:  # Decreasing by more than 5% per month
            pattern = 'decreasing'
        else:
            pattern = 'stable'
        
        # Determine volatility
        if volatility_ratio > 0.3:
            volatility = 'high'
        elif volatility_ratio > 0.15:
            volatility = 'medium'
        else:
            volatility = 'low'
        
        return {
            'pattern': pattern,
            'trend_strength': abs(slope),
            'average_monthly': round(average_monthly, 2),
            'volatility': volatility,
            'volatility_ratio': round(volatility_ratio, 2),
            'confidence': round(self.model.score(X, y) * 100, 1)
        }


def predict_next_day_expense(user):
    """
    Convenience function to predict next day's expense for a user.
    """
    engine = ExpenseForecastEngine(user)
    return engine.predict_next_day()


def predict_next_month_expense(user):
    """
    Convenience function to predict next month's expense for a user.
    """
    engine = ExpenseForecastEngine(user)
    return engine.predict_next_month_expense()


def get_expense_forecast_chart(user, months_ahead=4):
    """
    Get expense forecast chart data for visualization.
    """
    engine = ExpenseForecastEngine(user)
    return engine.get_forecast_chart_data(months_ahead)


def get_spending_analysis(user):
    """
    Get comprehensive spending pattern analysis.
    """
    engine = ExpenseForecastEngine(user)
    return engine.get_spending_pattern_analysis()
