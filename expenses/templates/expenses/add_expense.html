{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Expense - BudgetWise</title>
    <link rel="stylesheet" href="{% static 'css/modern-dashboard.css' %}">
</head>
<body>
    <div class="dashboard-layout">
        <!-- Sidebar -->
        {% include 'expenses/partials/sidebar.html' %}

        <!-- Main Content -->
        <main class="main-content">
            <header class="top-bar">
                <div class="top-bar-left">
                    <h1>Add New Expense</h1>
                    <p class="subtitle">Track your spending</p>
                </div>
                <div class="top-bar-right">
                    <a href="{% url 'expenses:dashboard' %}" class="btn btn-secondary">← Back to Dashboard</a>
                </div>
            </header>

            {% if messages %}
            <div class="messages-container">
                {% for message in messages %}
                <div class="alert alert-{{ message.tags }}">
                    {{ message }}
                    <button class="alert-close" onclick="this.parentElement.remove()">×</button>
                </div>
                {% endfor %}
            </div>
            {% endif %}

            <div class="form-container">
                <div class="form-card">
                    <form method="post" class="expense-form">
                        {% csrf_token %}
                        
                        <div class="form-group">
                            <label for="{{ form.date.id_for_label }}">Date</label>
                            {{ form.date }}
                            {% if form.date.errors %}
                                <div class="error-message">{{ form.date.errors.0 }}</div>
                            {% endif %}
                        </div>

                        <div class="form-group">
                            <label for="{{ form.amount.id_for_label }}">Amount (?)</label>
                            {{ form.amount }}
                            {% if form.amount.errors %}
                                <div class="error-message">{{ form.amount.errors.0 }}</div>
                            {% endif %}
                        </div>

                        <div class="form-group">
                            <label for="{{ form.category.id_for_label }}">Category</label>
                            {{ form.category }}
                            {% if form.category.errors %}
                                <div class="error-message">{{ form.category.errors.0 }}</div>
                            {% endif %}
                        </div>

                        <div class="form-group">
                            <label for="{{ form.description.id_for_label }}">Description</label>
                            {{ form.description }}
                            {% if form.description.errors %}
                                <div class="error-message">{{ form.description.errors.0 }}</div>
                            {% endif %}
                        </div>

                        <div class="form-actions">
                            <button type="submit" class="btn btn-primary btn-large">Add Expense</button>
                            <a href="{% url 'expenses:dashboard' %}" class="btn btn-secondary btn-large">Cancel</a>
                        </div>
                    </form>
                </div>
            </div>
        </main>
    </div>
</body>
</html>

