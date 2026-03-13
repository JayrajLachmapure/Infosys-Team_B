"""
Forms for user authentication.
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm, SetPasswordForm
from django.core.exceptions import ValidationError
import re


class SignUpForm(UserCreationForm):
    """
    Custom signup form with email validation and password requirements.
    """
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Email address'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-input',
            'placeholder': 'Username'
        })
    )
    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input password-input',
            'placeholder': 'Password',
            'id': 'id_password1'
        }),
        help_text=''
    )
    password2 = forms.CharField(
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input password-input',
            'placeholder': 'Confirm password',
            'id': 'id_password2'
        }),
        help_text=''
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        """
        Validate that the email is unique.
        """
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError('This email address is already registered.')
        return email

    def clean_username(self):
        """
        Validate that the username is unique and meets requirements.
        """
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError('This username is already taken.')
        if len(username) < 3:
            raise ValidationError('Username must be at least 3 characters long.')
        return username

    def clean_password1(self):
        """
        Validate password meets custom requirements.
        """
        password = self.cleaned_data.get('password1')
        
        if len(password) < 8:
            raise ValidationError('Password must be at least 8 characters long.')
        
        if not re.search(r'[A-Z]', password):
            raise ValidationError('Password must contain at least one uppercase letter.')
        
        if not re.search(r'[a-z]', password):
            raise ValidationError('Password must contain at least one lowercase letter.')
        
        if not re.search(r'[0-9]', password):
            raise ValidationError('Password must contain at least one number.')
        
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            raise ValidationError('Password must contain at least one special character (!@#$%^&*(),.?":{}|<>).')
        
        return password

    def save(self, commit=True):
        """
        Save the user with hashed password.
        """
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class CustomPasswordResetForm(PasswordResetForm):
    """
    Custom password reset form.
    """
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-input',
            'placeholder': 'Enter your email address'
        })
    )


class CustomSetPasswordForm(SetPasswordForm):
    """
    Custom set password form for password reset.
    """
    new_password1 = forms.CharField(
        label='New Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input password-input',
            'placeholder': 'New password',
            'id': 'id_new_password1'
        }),
        help_text=''
    )
    new_password2 = forms.CharField(
        label='Confirm New Password',
        widget=forms.PasswordInput(attrs={
            'class': 'form-input password-input',
            'placeholder': 'Confirm new password',
            'id': 'id_new_password2'
        }),
        help_text=''
    )
