"""
Models for accounts app.
Using Django's built-in User model - no custom models needed for Phase 1.
"""
from django.contrib.auth.models import User

# Django's built-in User model provides:
# - username
# - email
# - password (automatically hashed)
# - first_name, last_name
# - is_active, is_staff, is_superuser
# - date_joined, last_login
