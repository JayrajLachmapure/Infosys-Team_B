"""
URL patterns for AI engine.
"""
from django.urls import path
from . import views

app_name = 'ai_engine'

urlpatterns = [
    # API endpoints
    path('api/predict-expense/', views.PredictExpenseView.as_view(), name='predict_expense'),
    path('api/insights/', views.InsightsView.as_view(), name='insights'),
    path('api/forecast-chart/', views.ForecastChartDataView.as_view(), name='forecast_chart'),
    
    # Dashboard page
    path('ai-insights/', views.AIInsightsDashboardView.as_view(), name='ai_dashboard'),
]
