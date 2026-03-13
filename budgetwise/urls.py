"""
URL configuration for BudgetWise project.
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('expenses.urls')),
    path('ai/', include('ai_engine.urls')),
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
]
