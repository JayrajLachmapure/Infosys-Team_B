"""
Views for authentication system.
"""
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordResetView, PasswordResetConfirmView, PasswordResetDoneView, PasswordResetCompleteView
from django.contrib import messages
from django.views import View
from django.urls import reverse_lazy
from .forms import SignUpForm, CustomPasswordResetForm, CustomSetPasswordForm


class SignUpView(View):
    """
    Handle user registration.
    """
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('expenses:dashboard')
        form = SignUpForm()
        return render(request, 'accounts/signup.html', {'form': form})

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Account created successfully! Please log in.')
            return redirect('accounts:login')
        return render(request, 'accounts/signup.html', {'form': form})


class LoginView(View):
    """
    Handle user login.
    """
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('expenses:dashboard')
        return render(request, 'accounts/login.html')

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('expenses:dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
            return render(request, 'accounts/login.html')


class LogoutView(View):
    """
    Handle user logout.
    """
    def get(self, request):
        logout(request)
        messages.info(request, 'You have been logged out successfully.')
        return redirect('accounts:login')


class DashboardView(LoginRequiredMixin, View):
    """
    Placeholder dashboard - requires authentication.
    This demonstrates LoginRequiredMixin for future protected views.
    """
    def get(self, request):
        return render(request, 'accounts/dashboard.html', {
            'user': request.user
        })


class CustomPasswordResetView(PasswordResetView):
    """
    Custom password reset view.
    """
    form_class = CustomPasswordResetForm
    template_name = 'accounts/password_reset.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject.txt'
    success_url = reverse_lazy('accounts:password_reset_done')


class CustomPasswordResetDoneView(PasswordResetDoneView):
    """
    Password reset email sent confirmation.
    """
    template_name = 'accounts/password_reset_done.html'


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    """
    Password reset confirmation view.
    """
    form_class = CustomSetPasswordForm
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    """
    Password reset complete view.
    """
    template_name = 'accounts/password_reset_complete.html'
