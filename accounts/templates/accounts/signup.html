{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Sign Up - BudgetWise</title>
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>
<body>
    <div class="auth-container">
        <div class="auth-header">
            <h1>Create Account</h1>
            <p>Join BudgetWise and start managing your finances</p>
        </div>

        {% if messages %}
        <div class="messages">
            {% for message in messages %}
            <div class="alert alert-{{ message.tags }}">
                {{ message }}
            </div>
            {% endfor %}
        </div>
        {% endif %}

        <form method="post" action="{% url 'accounts:signup' %}">
            {% csrf_token %}
            
            <div class="form-group {% if form.username.errors %}error{% endif %}">
                <label for="{{ form.username.id_for_label }}">Username</label>
                {{ form.username }}
                {% if form.username.errors %}
                    <ul class="errorlist">
                    {% for error in form.username.errors %}
                        <li>{{ error }}</li>
                    {% endfor %}
                    </ul>
                {% endif %}
            </div>

            <div class="form-group {% if form.email.errors %}error{% endif %}">
                <label for="{{ form.email.id_for_label }}">Email</label>
                {{ form.email }}
                {% if form.email.errors %}
                    <ul class="errorlist">
                    {% for error in form.email.errors %}
                        <li>{{ error }}</li>
                    {% endfor %}
                    </ul>
                {% endif %}
            </div>

            <div class="form-group {% if form.password1.errors %}error{% endif %}">
                <label for="{{ form.password1.id_for_label }}">Password</label>
                <div class="password-wrapper">
                    {{ form.password1 }}
                    <span class="password-toggle" onclick="togglePassword('id_password1', this)">
                        <svg class="eye-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                            <circle cx="12" cy="12" r="3"></circle>
                        </svg>
                    </span>
                </div>
                <div class="password-requirements">
                    <p class="requirements-title">Password must contain:</p>
                    <ul>
                        <li>✓ Minimum 8 characters</li>
                        <li>✓ At least one uppercase letter (A-Z)</li>
                        <li>✓ At least one lowercase letter (a-z)</li>
                        <li>✓ At least one number (0-9)</li>
                        <li>✓ At least one special character (!@#$%^&*)</li>
                    </ul>
                </div>
                {% if form.password1.errors %}
                    <ul class="errorlist">
                    {% for error in form.password1.errors %}
                        <li>{{ error }}</li>
                    {% endfor %}
                    </ul>
                {% endif %}
            </div>

            <div class="form-group {% if form.password2.errors %}error{% endif %}">
                <label for="{{ form.password2.id_for_label }}">Confirm Password</label>
                <div class="password-wrapper">
                    {{ form.password2 }}
                    <span class="password-toggle" onclick="togglePassword('id_password2', this)">
                        <svg class="eye-icon" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor">
                            <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path>
                            <circle cx="12" cy="12" r="3"></circle>
                        </svg>
                    </span>
                </div>
                {% if form.password2.errors %}
                    <ul class="errorlist">
                    {% for error in form.password2.errors %}
                        <li>{{ error }}</li>
                    {% endfor %}
                    </ul>
                {% endif %}
            </div>

            {% if form.non_field_errors %}
            <div class="alert alert-error">
                {% for error in form.non_field_errors %}
                    {{ error }}
                {% endfor %}
            </div>
            {% endif %}

            <button type="submit" class="btn btn-primary">Create Account</button>
        </form>

        <div class="form-footer">
            <p>Already have an account? <a href="{% url 'accounts:login' %}">Sign in</a></p>
        </div>
    </div>

    <script>
        function togglePassword(inputId, icon) {
            const input = document.getElementById(inputId);
            const eyeIcon = icon.querySelector('.eye-icon');
            
            if (input.type === 'password') {
                input.type = 'text';
                eyeIcon.innerHTML = '<path d="M17.94 17.94A10.07 10.07 0 0 1 12 20c-7 0-11-8-11-8a18.45 18.45 0 0 1 5.06-5.94M9.9 4.24A9.12 9.12 0 0 1 12 4c7 0 11 8 11 8a18.5 18.5 0 0 1-2.16 3.19m-6.72-1.07a3 3 0 1 1-4.24-4.24"></path><line x1="1" y1="1" x2="23" y2="23"></line>';
            } else {
                input.type = 'password';
                eyeIcon.innerHTML = '<path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"></path><circle cx="12" cy="12" r="3"></circle>';
            }
        }
    </script>
</body>
</html>
