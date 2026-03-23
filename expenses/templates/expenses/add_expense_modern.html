{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Add Expense - BudgetWise AI</title>
    <link rel="stylesheet" href="{% static 'css/dashboard-modern.css' %}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
</head>
<body>
    <div class="dashboard-container">
        <!-- Sidebar -->
        <aside class="sidebar">
            <div class="sidebar-header">
                <div class="sidebar-logo">
                    <div class="sidebar-logo-icon">
                        <i class="fas fa-chart-line"></i>
                    </div>
                    <div>
                        <div class="sidebar-title">BudgetWise AI</div>
                        <div class="sidebar-subtitle">Smart Finance Tracking</div>
                    </div>
                </div>
            </div>
            
            <nav class="sidebar-nav">
                <a href="{% url 'expenses:dashboard' %}" class="nav-item">
                    <div class="nav-icon">
                        <i class="fas fa-tachometer-alt"></i>
                    </div>
                    <span>Dashboard</span>
                </a>
                <a href="{% url 'expenses:add_expense' %}" class="nav-item active">
                    <div class="nav-icon">
                        <i class="fas fa-plus-circle"></i>
                    </div>
                    <span>Add Expense</span>
                </a>
                <a href="{% url 'expenses:list_expenses' %}" class="nav-item">
                    <div class="nav-icon">
                        <i class="fas fa-list-alt"></i>
                    </div>
                    <span>All Expenses</span>
                </a>
                <a href="{% url 'expenses:analytics' %}" class="nav-item">
                    <div class="nav-icon">
                        <i class="fas fa-chart-bar"></i>
                    </div>
                    <span>Analytics</span>
                </a>
            </nav>
            
            <div class="sidebar-footer">
                <div class="user-info">
                    <div class="user-avatar">{{ user.username|slice:":1"|upper }}</div>
                    <div class="user-details">
                        <div class="user-name">{{ user.username|title }}</div>
                        <div class="user-email">{{ user.email }}</div>
                    </div>
                </div>
                <a href="{% url 'accounts:logout' %}" class="btn-logout">
                    <i class="fas fa-sign-out-alt"></i>
                    <span>Logout</span>
                </a>
            </div>
        </aside>

        <!-- Main Content -->
        <main class="main-content">
            <!-- Page Header -->
            <div class="dashboard-header">
                <h1 class="dashboard-title">Add New Expense</h1>
                <p class="dashboard-subtitle">Track your spending and maintain your budget</p>
            </div>

            <!-- Messages -->
            {% if messages %}
            <div class="messages-container">
                {% for message in messages %}
                <div class="alert alert-{{ message.tags }}">
                    <div class="alert-icon">
                        {% if message.tags == 'success' %}
                            <i class="fas fa-check-circle"></i>
                        {% elif message.tags == 'error' %}
                            <i class="fas fa-exclamation-circle"></i>
                        {% else %}
                            <i class="fas fa-info-circle"></i>
                        {% endif %}
                    </div>
                    <div class="alert-content">
                        <div class="alert-message">{{ message }}</div>
                    </div>
                </div>
                {% endfor %}
            </div>
            {% endif %}

            <!-- Form Container -->
            <div class="form-container">
                <div class="form-card">
                    <div class="form-header">
                        <div class="form-icon">
                            <i class="fas fa-plus-circle"></i>
                        </div>
                        <div>
                            <h2 class="form-title">Expense Details</h2>
                            <p class="form-subtitle">Enter the details of your expense</p>
                        </div>
                    </div>

                    <form method="post" class="modern-form">
                        {% csrf_token %}
                        
                        <div class="form-grid">
                            <div class="form-group">
                                <label for="{{ form.date.id_for_label }}" class="form-label">
                                    <i class="fas fa-calendar-alt"></i>
                                    Date
                                </label>
                                {{ form.date }}
                                {% if form.date.errors %}
                                    <div class="error-message">
                                        <i class="fas fa-exclamation-triangle"></i>
                                        {{ form.date.errors.0 }}
                                    </div>
                                {% endif %}
                            </div>

                            <div class="form-group">
                                <label for="{{ form.amount.id_for_label }}" class="form-label">
                                    <i class="fas fa-rupee-sign"></i>
                                    Amount (₹)
                                </label>
                                {{ form.amount }}
                                {% if form.amount.errors %}
                                    <div class="error-message">
                                        <i class="fas fa-exclamation-triangle"></i>
                                        {{ form.amount.errors.0 }}
                                    </div>
                                {% endif %}
                            </div>

                            <div class="form-group">
                                <label for="{{ form.category.id_for_label }}" class="form-label">
                                    <i class="fas fa-tags"></i>
                                    Category
                                </label>
                                {{ form.category }}
                                {% if form.category.errors %}
                                    <div class="error-message">
                                        <i class="fas fa-exclamation-triangle"></i>
                                        {{ form.category.errors.0 }}
                                    </div>
                                {% endif %}
                            </div>

                            <div class="form-group form-group-full">
                                <label for="{{ form.description.id_for_label }}" class="form-label">
                                    <i class="fas fa-align-left"></i>
                                    Description
                                </label>
                                {{ form.description }}
                                {% if form.description.errors %}
                                    <div class="error-message">
                                        <i class="fas fa-exclamation-triangle"></i>
                                        {{ form.description.errors.0 }}
                                    </div>
                                {% endif %}
                            </div>
                        </div>

                        <div class="form-actions">
                            <button type="submit" class="btn-primary btn-large">
                                <i class="fas fa-plus"></i>
                                Add Expense
                            </button>
                            <a href="{% url 'expenses:dashboard' %}" class="btn-secondary btn-large">
                                <i class="fas fa-arrow-left"></i>
                                Back to Dashboard
                            </a>
                        </div>
                    </form>
                </div>

                <!-- Quick Tips -->
                <div class="tips-card">
                    <div class="tips-header">
                        <div class="tips-icon">
                            <i class="fas fa-lightbulb"></i>
                        </div>
                        <h3 class="tips-title">Quick Tips</h3>
                    </div>
                    <div class="tips-content">
                        <div class="tip-item">
                            <i class="fas fa-check"></i>
                            <span>Choose the most specific category for better insights</span>
                        </div>
                        <div class="tip-item">
                            <i class="fas fa-check"></i>
                            <span>Add detailed descriptions for easier tracking</span>
                        </div>
                        <div class="tip-item">
                            <i class="fas fa-check"></i>
                            <span>Regular tracking helps AI provide better predictions</span>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </div>

    <style>
        .form-container {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 32px;
            max-width: 1200px;
        }

        .form-card {
            background: var(--card-background);
            border-radius: var(--radius-lg);
            padding: 32px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-color);
        }

        .form-header {
            display: flex;
            align-items: center;
            gap: 16px;
            margin-bottom: 32px;
            padding-bottom: 24px;
            border-bottom: 1px solid var(--border-color);
        }

        .form-icon {
            width: 48px;
            height: 48px;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-hover) 100%);
            border-radius: var(--radius-lg);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 24px;
        }

        .form-title {
            font-size: 24px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 4px;
        }

        .form-subtitle {
            font-size: 14px;
            color: var(--text-secondary);
        }

        .modern-form {
            display: flex;
            flex-direction: column;
            gap: 24px;
        }

        .form-grid {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 24px;
        }

        .form-group-full {
            grid-column: 1 / -1;
        }

        .form-group {
            display: flex;
            flex-direction: column;
            gap: 8px;
        }

        .form-label {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
            font-weight: 600;
            color: var(--text-primary);
        }

        .form-label i {
            color: var(--primary-color);
        }

        .form-group input,
        .form-group select,
        .form-group textarea {
            padding: 12px 16px;
            border: 1px solid var(--border-color);
            border-radius: var(--radius-md);
            font-size: 14px;
            transition: all 0.2s ease;
            background: white;
            font-family: inherit;
        }

        .form-group input:focus,
        .form-group select:focus,
        .form-group textarea:focus {
            outline: none;
            border-color: var(--primary-color);
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
        }

        .form-group textarea {
            resize: vertical;
            min-height: 80px;
        }

        .error-message {
            display: flex;
            align-items: center;
            gap: 6px;
            color: var(--accent-danger);
            font-size: 12px;
            font-weight: 500;
        }

        .form-actions {
            display: flex;
            gap: 16px;
            padding-top: 24px;
            border-top: 1px solid var(--border-color);
        }

        .btn-large {
            padding: 14px 28px;
            font-size: 16px;
            font-weight: 600;
            border-radius: var(--radius-md);
            text-decoration: none;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            transition: all 0.2s ease;
            border: none;
            cursor: pointer;
        }

        .btn-secondary {
            background: var(--background-color);
            color: var(--text-primary);
            border: 1px solid var(--border-color);
        }

        .btn-secondary:hover {
            background: white;
            box-shadow: var(--shadow-sm);
        }

        .tips-card {
            background: var(--card-background);
            border-radius: var(--radius-lg);
            padding: 24px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-color);
            height: fit-content;
        }

        .tips-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }

        .tips-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--accent-warning) 0%, #d97706 100%);
            border-radius: var(--radius-lg);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 18px;
        }

        .tips-title {
            font-size: 18px;
            font-weight: 600;
            color: var(--text-primary);
        }

        .tips-content {
            display: flex;
            flex-direction: column;
            gap: 12px;
        }

        .tip-item {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 14px;
            color: var(--text-secondary);
        }

        .tip-item i {
            color: var(--accent-success);
            font-size: 12px;
        }

        @media (max-width: 768px) {
            .form-container {
                grid-template-columns: 1fr;
                gap: 24px;
            }

            .form-grid {
                grid-template-columns: 1fr;
                gap: 20px;
            }

            .form-actions {
                flex-direction: column;
            }

            .form-card {
                padding: 24px;
            }
        }
    </style>
</body>
</html>