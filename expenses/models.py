"""
Models for expense tracking and budget management.
"""
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from decimal import Decimal
from django.utils import timezone


class Budget(models.Model):
    """
    Monthly budget for a user.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='budgets')
    month = models.CharField(max_length=7, help_text="Format: YYYY-MM")
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'month')
        ordering = ['-month']

    def __str__(self):
        return f"{self.user.username} - {self.month}: ${self.amount}"


class Expense(models.Model):
    """
    Individual expense entry with enhanced categorization.
    """
    CATEGORY_CHOICES = [
        ('Food', '🍔 Food'),
        ('Transport', '🚗 Transport'),
        ('Rent', '🏠 Rent'),
        ('Shopping', '🛍️ Shopping'),
        ('Entertainment', '🎬 Entertainment'),
        ('Bills', '💡 Bills'),
        ('Healthcare', '🏥 Healthcare'),
        ('Education', '📚 Education'),
        ('Travel', '✈️ Travel'),
        ('Groceries', '🛒 Groceries'),
        ('Utilities', '⚡ Utilities'),
        ('Other', '📦 Other'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.01'))]
    )
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True, null=True, help_text="Optional description")
    date = models.DateField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date', '-created_at']
        indexes = [
            models.Index(fields=['user', 'date']),
            models.Index(fields=['user', 'category']),
        ]

    def __str__(self):
        return f"{self.user.username} - {self.category}: ${self.amount} on {self.date}"

    def get_category_icon(self):
        """Return emoji icon for category"""
        icons = {
            'Food': '🍔',
            'Transport': '🚗',
            'Rent': '🏠',
            'Shopping': '🛍️',
            'Entertainment': '🎬',
            'Bills': '💡',
            'Healthcare': '🏥',
            'Education': '📚',
            'Travel': '✈️',
            'Groceries': '🛒',
            'Utilities': '⚡',
            'Other': '📦',
        }
        return icons.get(self.category, '📦')
