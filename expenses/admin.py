"""
Admin configuration for expenses app.
"""
from django.contrib import admin
from .models import Budget, Expense


@admin.register(Budget)
class BudgetAdmin(admin.ModelAdmin):
    list_display = ('user', 'month', 'amount', 'created_at')
    list_filter = ('month', 'created_at')
    search_fields = ('user__username', 'month')


@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('user', 'category', 'amount', 'date', 'created_at')
    list_filter = ('category', 'date', 'created_at')
    search_fields = ('user__username', 'category', 'note')
    date_hierarchy = 'date'
