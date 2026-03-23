"""
URL patterns for expenses app.
"""
from django.urls import path
from . import views

app_name = 'expenses'

urlpatterns = [
    # Main pages
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('add-expense/', views.AddExpenseView.as_view(), name='add_expense'),
    path('edit-expense/<int:expense_id>/', views.EditExpenseView.as_view(), name='edit_expense'),
    path('delete-expense/<int:expense_id>/', views.DeleteExpenseView.as_view(), name='delete_expense'),
    path('expenses/', views.ListExpensesView.as_view(), name='list_expenses'),
    path('analytics/', views.AnalyticsView.as_view(), name='analytics'),
    path('set-budget/', views.SetBudgetView.as_view(), name='set_budget'),
    path('budget-management/', views.BudgetManagementView.as_view(), name='budget_management'),
    
    # API endpoints for charts
    path('api/category-chart/', views.CategoryChartDataView.as_view(), name='category_chart'),
    path('api/monthly-chart/', views.MonthlyChartDataView.as_view(), name='monthly_chart'),
    path('api/trend-chart/', views.TrendChartDataView.as_view(), name='trend_chart'),
]
