"""
AI Engine Views
API endpoints for expense forecasting and insights.
"""
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.http import JsonResponse
from .forecast import predict_next_day_expense, predict_next_month_expense, get_expense_forecast_chart, ExpenseForecastEngine
from .insights import generate_user_insights, FinancialInsightsEngine


class PredictExpenseView(LoginRequiredMixin, View):
    """
    API endpoint to predict next month's expense.
    """
    def get(self, request):
        prediction = predict_next_day_expense(request.user)
        return JsonResponse(prediction)


class InsightsView(LoginRequiredMixin, View):
    """
    API endpoint to get financial insights.
    """
    def get(self, request):
        insights = generate_user_insights(request.user)
        
        # Convert Decimal to float for JSON serialization
        def convert_decimals(obj):
            if isinstance(obj, dict):
                return {k: convert_decimals(v) for k, v in obj.items()}
            elif isinstance(obj, list):
                return [convert_decimals(item) for item in obj]
            elif hasattr(obj, '__float__'):
                return float(obj)
            return obj
        
        insights = convert_decimals(insights)
        return JsonResponse(insights)


class ForecastChartDataView(LoginRequiredMixin, View):
    """
    API endpoint for forecast chart data.
    Returns historical data + prediction.
    """
    def get(self, request):
        engine = ExpenseForecastEngine(request.user)
        
        # Get historical data
        df = engine.get_historical_data(days=30)
        
        if df is None:
            return JsonResponse({
                'success': False,
                'message': 'No historical data available'
            })
        
        # Get prediction
        prediction = engine.predict_next_day()
        
        # Prepare chart data
        historical_labels = [row['date'].strftime('%b %d') for _, row in df.iterrows()]
        historical_data = df['total'].tolist()
        
        # Add prediction point
        if prediction['success']:
            from datetime import datetime, timedelta
            
            next_day = datetime.now() + timedelta(days=1)
            prediction_label = next_day.strftime('%b %d')
            prediction_value = prediction['predicted_amount']
            
            return JsonResponse({
                'success': True,
                'historical_labels': historical_labels,
                'historical_data': historical_data,
                'prediction_label': prediction_label,
                'prediction_value': prediction_value,
                'confidence': prediction['confidence']
            })
        
        return JsonResponse({
            'success': True,
            'historical_labels': historical_labels,
            'historical_data': historical_data,
            'prediction_label': None,
            'prediction_value': None
        })


class AIInsightsDashboardView(LoginRequiredMixin, View):
    """
    Render AI insights dashboard page.
    """
    def get(self, request):
        # Get prediction
        prediction = predict_next_day_expense(request.user)
        
        # Get insights
        insights_engine = FinancialInsightsEngine(request.user)
        insights = insights_engine.generate_user_insights()
        
        context = {
            'prediction': prediction,
            'insights': insights
        }
        
        return render(request, 'ai_engine/ai_insights_modern.html', context)
