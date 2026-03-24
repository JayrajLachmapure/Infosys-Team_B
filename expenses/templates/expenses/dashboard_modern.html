{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard - BudgetWise AI</title>
    <link rel="stylesheet" href="{% static 'css/dashboard-modern.css' %}">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
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
                <a href="{% url 'expenses:dashboard' %}{% if selected_month %}?month={{ selected_month }}{% endif %}" class="nav-item active">
                    <div class="nav-icon">
                        <i class="fas fa-tachometer-alt"></i>
                    </div>
                    <span>Dashboard</span>
                </a>
                <a href="{% url 'expenses:add_expense' %}" class="nav-item">
                    <div class="nav-icon">
                        <i class="fas fa-plus-circle"></i>
                    </div>
                    <span>Add Expense</span>
                </a>
                <a href="{% url 'expenses:list_expenses' %}{% if selected_month %}?month={{ selected_month }}{% endif %}" class="nav-item">
                    <div class="nav-icon">
                        <i class="fas fa-list-alt"></i>
                    </div>
                    <span>All Expenses</span>
                </a>
                <a href="{% url 'expenses:analytics' %}{% if selected_month %}?month={{ selected_month }}{% endif %}" class="nav-item">
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
            <!-- Dashboard Header -->
            <div class="dashboard-header">
                <div class="header-content">
                    <div class="header-left">
                        <h1 class="dashboard-title">Financial Dashboard</h1>
                        <p class="dashboard-subtitle">Welcome back, {{ user.username|title }}! Here's your financial overview for {{ selected_month_display }}.</p>
                    </div>
                    <div class="header-right">
                        <div class="month-selector">
                            <label for="month-select" class="month-label">View Month:</label>
                            <select id="month-select" class="month-select" onchange="changeMonth(this.value)">
                                {% for month_value, month_display in month_choices %}
                                <option value="{{ month_value }}" {% if month_value == selected_month %}selected{% endif %}>
                                    {{ month_display }}
                                </option>
                                {% endfor %}
                            </select>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Usage Alerts -->
            {% for alert in summary.usage_alerts %}
            <div class="alert alert-{{ alert.type }}">
                <div class="alert-icon">{{ alert.icon }}</div>
                <div class="alert-content">
                    <div class="alert-title">{{ alert.title }}</div>
                    <div class="alert-message">{{ alert.message }}</div>
                    {% if alert.progress > 0 %}
                    <div class="progress-bar">
                        <div class="progress-fill progress-{{ alert.type }}" style="width: {{ alert.progress }}%"></div>
                    </div>
                    {% endif %}
                </div>
            </div>
            {% endfor %}

            <!-- Summary Cards -->
            <div class="summary-grid">
                <!-- Total Expenses Card -->
                <div class="summary-card fade-in">
                    <div class="card-header">
                        <div class="card-icon expenses">
                            <i class="fas fa-wallet"></i>
                        </div>
                        <div class="card-menu">
                            <i class="fas fa-ellipsis-h"></i>
                        </div>
                    </div>
                    <div class="card-content">
                        <div class="card-value">{{ kpi_data.total_expenses.formatted }}</div>
                        <div class="card-label">Total Expenses</div>
                    </div>
                    <div class="card-footer">
                        <div class="card-trend neutral">
                            <i class="fas fa-calendar-alt"></i>
                            <span>{{ selected_month_display }}</span>
                        </div>
                    </div>
                </div>

                <!-- Total Savings Card -->
                <div class="summary-card fade-in">
                    <div class="card-header">
                        <div class="card-icon savings">
                            <i class="fas fa-piggy-bank"></i>
                        </div>
                        <div class="card-menu">
                            <i class="fas fa-ellipsis-h"></i>
                        </div>
                    </div>
                    <div class="card-content">
                        <div class="card-value">₹{{ summary.total_savings.total_savings|floatformat:0 }}</div>
                        <div class="card-label">Total Savings</div>
                    </div>
                    <div class="card-footer">
                        <div class="card-trend positive">
                            <i class="fas fa-arrow-up"></i>
                            <span>{{ summary.total_savings.savings_rate }}% saved</span>
                        </div>
                        <div class="card-period">Last 12 months</div>
                    </div>
                </div>

                <!-- Transactions Card -->
                <div class="summary-card fade-in">
                    <div class="card-header">
                        <div class="card-icon transactions">
                            <i class="fas fa-exchange-alt"></i>
                        </div>
                        <div class="card-menu">
                            <i class="fas fa-ellipsis-h"></i>
                        </div>
                    </div>
                    <div class="card-content">
                        <div class="card-value">{{ kpi_data.transaction_count.value }}</div>
                        <div class="card-label">Transactions</div>
                    </div>
                    <div class="card-footer">
                        <div class="card-trend neutral">
                            <i class="fas fa-calendar-alt"></i>
                            <span>{{ selected_month_display }}</span>
                        </div>
                    </div>
                </div>

                <!-- Top Category Card -->
                <div class="summary-card fade-in">
                    <div class="card-header">
                        <div class="card-icon category">
                            <i class="fas fa-trophy"></i>
                        </div>
                        <div class="card-menu">
                            <i class="fas fa-ellipsis-h"></i>
                        </div>
                    </div>
                    <div class="card-content">
                        <div class="card-value">{{ summary.highest_category.category }}</div>
                        <div class="card-label">Top Category</div>
                    </div>
                    <div class="card-footer">
                        <div class="card-trend neutral">
                            <i class="fas fa-rupee-sign"></i>
                            <span>₹{{ summary.highest_category.amount|floatformat:0 }}</span>
                        </div>
                    </div>
                </div>

                <!-- Savings Ratio Card -->
                <div class="summary-card fade-in">
                    <div class="card-header">
                        <div class="card-icon savings-ratio">
                            <i class="fas fa-chart-line"></i>
                        </div>
                        <div class="card-menu">
                            <i class="fas fa-ellipsis-h"></i>
                        </div>
                    </div>
                    <div class="card-content">
                        <div class="card-value">{{ kpi_data.savings_ratio.ratio }}%</div>
                        <div class="card-label">Savings Ratio</div>
                    </div>
                    <div class="card-footer">
                        <div class="card-trend {{ kpi_data.savings_ratio.trend }}">
                            {% if kpi_data.savings_ratio.trend == 'positive' %}
                                <i class="fas fa-arrow-up"></i>
                                <span>{{ kpi_data.savings_ratio.comparison_text }}</span>
                            {% elif kpi_data.savings_ratio.trend == 'negative' %}
                                <i class="fas fa-arrow-down"></i>
                                <span>{{ kpi_data.savings_ratio.comparison_text }}</span>
                            {% else %}
                                <i class="fas fa-minus"></i>
                                <span>{{ kpi_data.savings_ratio.comparison_text }}</span>
                            {% endif %}
                        </div>
                    </div>
                </div>
            </div>

            <!-- AI Insights Section -->
            <div class="ai-insights fade-in">
                <div class="ai-header">
                    <div class="ai-icon">
                        <i class="fas fa-brain"></i>
                    </div>
                    <div>
                        <div class="ai-title">AI Financial Insights</div>
                        <div class="ai-subtitle">Powered by machine learning analytics</div>
                    </div>
                </div>

                <div class="insights-grid">
                    <!-- AI Prediction -->
                    <div class="insight-card">
                        <div class="insight-header">
                            <div class="insight-icon">
                                <i class="fas fa-crystal-ball"></i>
                            </div>
                            <div class="insight-title">
                                {% if is_current_month %}
                                    Next Day Prediction
                                {% elif is_future_month %}
                                    Future Month
                                {% else %}
                                    Historical Data
                                {% endif %}
                            </div>
                        </div>
                        <div class="insight-content">
                            {% if is_current_month and ai_prediction.success %}
                                <div class="insight-value">₹{{ ai_prediction.predicted_amount }}</div>
                                <p>Based on your last 10 days of spending patterns</p>
                                <small>Confidence: {{ ai_prediction.confidence }}% • Trend: {{ ai_prediction.trend|title }}</small>
                            {% else %}
                                <p>{{ ai_prediction.message }}</p>
                                {% if is_current_month %}
                                    <small>Add more expense data to enable predictions</small>
                                {% endif %}
                            {% endif %}
                        </div>
                    </div>

                    <!-- Monthly Expense Forecast -->
                    <div class="insight-card">
                        <div class="insight-header">
                            <div class="insight-icon">
                                <i class="fas fa-calendar-alt"></i>
                            </div>
                            <div class="insight-title">Next Month Forecast</div>
                        </div>
                        <div class="insight-content">
                            {% if ai_monthly_forecast.success %}
                                <div class="insight-value">{{ ai_monthly_forecast.predicted_amount_formatted }}</div>
                                <p>
                                    {% if ai_monthly_forecast.percentage_change > 0 %}
                                        <span style="color: #EF4444;">+{{ ai_monthly_forecast.percentage_change }}%</span> compared to current month
                                    {% elif ai_monthly_forecast.percentage_change < 0 %}
                                        <span style="color: #10B981;">{{ ai_monthly_forecast.percentage_change }}%</span> compared to current month
                                    {% else %}
                                        <span style="color: #6B7280;">Similar to current month</span>
                                    {% endif %}
                                </p>
                                <small>Confidence: {{ ai_monthly_forecast.confidence }}% • Trend: {{ ai_monthly_forecast.trend|title }}</small>
                            {% else %}
                                <p>{{ ai_monthly_forecast.message }}</p>
                                <small>Add more monthly data to enable forecasting</small>
                            {% endif %}
                        </div>
                    </div>

                    <!-- Spending Analysis -->
                    <div class="insight-card">
                        <div class="insight-header">
                            <div class="insight-icon">
                                <i class="fas fa-chart-line"></i>
                            </div>
                            <div class="insight-title">Spending Analysis</div>
                        </div>
                        <div class="insight-content">
                            <p>{{ ai_insights.spending_change.message }}</p>
                            {% if ai_insights.overspending_alert.is_overspending %}
                                <div class="insight-value" style="color: #FCA5A5;">
                                    {{ ai_insights.overspending_alert.percentage_above_average }}%
                                </div>
                                <small>Above average spending</small>
                            {% endif %}
                        </div>
                    </div>

                    <!-- Smart Recommendations -->
                    <div class="insight-card">
                        <div class="insight-header">
                            <div class="insight-icon">
                                <i class="fas fa-lightbulb"></i>
                            </div>
                            <div class="insight-title">Smart Recommendations</div>
                        </div>
                        <div class="insight-content">
                            {% for advice in ai_insights.savings_advice|slice:":2" %}
                                <p>{{ advice.message }}</p>
                            {% endfor %}
                        </div>
                    </div>
                </div>
            </div>

            <!-- AI Expense Forecast Chart -->
            {% if ai_forecast_chart and ai_forecast_chart.chart_data_json %}
            <div class="forecast-section fade-in">
                <div class="section-header">
                    <h2 class="section-title">
                        <i class="fas fa-chart-line"></i>
                        AI Expense Forecast
                    </h2>
                    <p class="section-subtitle">Machine learning predictions based on your spending patterns</p>
                </div>
                
                <div class="forecast-chart-container">
                    <canvas id="forecastChart" width="400" height="200"></canvas>
                </div>
                
                <div class="forecast-legend">
                    <div class="legend-item">
                        <div class="legend-color" style="background-color: #3B82F6;"></div>
                        <span>Historical Data</span>
                    </div>
                    <div class="legend-item">
                        <div class="legend-color" style="background-color: #EF4444;"></div>
                        <span>AI Predictions</span>
                    </div>
                </div>
            </div>
            {% else %}
            <div class="forecast-section fade-in">
                <div class="section-header">
                    <h2 class="section-title">
                        <i class="fas fa-chart-line"></i>
                        AI Expense Forecast
                    </h2>
                    <p class="section-subtitle">Loading AI predictions... Please refresh if this persists.</p>
                </div>
            </div>
            {% endif %}
            <!-- Monthly Breakdown -->
            <div class="monthly-section">
                <div class="section-header">
                    <h2 class="section-title">
                        <i class="fas fa-calendar-alt"></i>
                        Monthly Breakdown
                    </h2>
                </div>
                <div class="monthly-grid">
                    {% for month in summary.monthly_breakdown|slice:":6" %}
                    <div class="month-card fade-in">
                        <div class="month-header">
                            <div class="month-title">{{ month.month }}</div>
                            <div class="month-status {% if month.savings >= 0 %}positive{% else %}negative{% endif %}">
                                {% if month.savings >= 0 %}
                                    <i class="fas fa-check-circle"></i> Saved
                                {% else %}
                                    <i class="fas fa-exclamation-triangle"></i> Over Budget
                                {% endif %}
                            </div>
                        </div>
                        <div class="month-stats">
                            <div class="stat-item">
                                <div class="stat-value">₹{{ month.expenses|floatformat:0 }}</div>
                                <div class="stat-label">Expenses</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value">₹{{ month.budget|floatformat:0 }}</div>
                                <div class="stat-label">Budget</div>
                            </div>
                            <div class="stat-item">
                                <div class="stat-value" style="color: {% if month.savings >= 0 %}#10B981{% else %}#EF4444{% endif %}">
                                    ₹{{ month.savings|floatformat:0 }}
                                </div>
                                <div class="stat-label">Savings</div>
                            </div>
                        </div>
                        {% if month.budget > 0 %}
                        <div class="progress-bar">
                            <div class="progress-fill {% if month.savings >= 0 %}progress-success{% else %}progress-danger{% endif %}" 
                                 style="width: {{ month.usage_percentage }}%"></div>
                        </div>
                        {% endif %}
                    </div>
                    {% empty %}
                    <div class="empty-state">
                        <div class="empty-icon">
                            <i class="fas fa-calendar-times"></i>
                        </div>
                        <div class="empty-title">No Monthly Data</div>
                        <div class="empty-message">Add some expenses and set budgets to see monthly breakdown</div>
                    </div>
                    {% endfor %}
                </div>
            </div>

            <!-- Budget Management -->
            <div class="budget-section fade-in">
                <div class="budget-header">
                    <div class="budget-icon">
                        <i class="fas fa-bullseye"></i>
                    </div>
                    <div class="budget-title">Budget Management</div>
                </div>
                
                <form method="post" action="{% url 'expenses:set_budget' %}" class="budget-form">
                    {% csrf_token %}
                    <div class="form-group">
                        <label class="form-label">{{ budget_form.month.label }}</label>
                        {{ budget_form.month }}
                    </div>
                    <div class="form-group">
                        <label class="form-label">{{ budget_form.amount.label }}</label>
                        {{ budget_form.amount }}
                    </div>
                    <button type="submit" class="btn-primary">
                        <i class="fas fa-save"></i>
                        Set Budget
                    </button>
                </form>
            </div>

            <!-- Quick Actions -->
            <div class="actions-section fade-in">
                <div class="actions-header">
                    <div class="actions-icon">
                        <i class="fas fa-bolt"></i>
                    </div>
                    <div class="actions-title">Quick Actions</div>
                </div>
                
                <div class="actions-grid">
                    <a href="{% url 'expenses:add_expense' %}" class="action-btn primary">
                        <i class="fas fa-plus"></i>
                        Add Expense
                    </a>
                    <a href="{% url 'expenses:list_expenses' %}" class="action-btn secondary">
                        <i class="fas fa-list"></i>
                        View All Expenses
                    </a>
                    <a href="{% url 'expenses:analytics' %}{% if selected_month %}?month={{ selected_month }}{% endif %}" class="action-btn secondary">
                        <i class="fas fa-chart-bar"></i>
                        Advanced Analytics
                    </a>
                    <a href="{% url 'accounts:logout' %}" class="action-btn danger">
                        <i class="fas fa-sign-out-alt"></i>
                        Logout
                    </a>
                </div>
            </div>
        </main>
    </div>

    <!-- Chart Scripts -->
    <script>
        // Modern chart configuration
        Chart.defaults.font.family = 'Inter, sans-serif';
        Chart.defaults.color = '#6B7280';
        Chart.defaults.borderColor = '#E5E7EB';
        Chart.defaults.backgroundColor = 'rgba(79, 70, 229, 0.1)';

        // AI Expense Forecast Chart
        {% if ai_forecast_chart and ai_forecast_chart.chart_data_json %}
        document.addEventListener('DOMContentLoaded', function() {
            const forecastCanvas = document.getElementById('forecastChart');
            if (forecastCanvas) {
                const ctx = forecastCanvas.getContext('2d');
                const chartData = {{ ai_forecast_chart.chart_data_json|safe }};
                
                if (chartData && chartData.length > 0) {
                    const historicalData = chartData.filter(item => !item.is_predicted);
                    const predictedData = chartData.filter(item => item.is_predicted);
                    
                    new Chart(ctx, {
                        type: 'line',
                        data: {
                            labels: chartData.map(item => item.month_name),
                            datasets: [{
                                label: 'Historical Expenses',
                                data: historicalData.map(item => item.total),
                                borderColor: '#3B82F6',
                                backgroundColor: 'rgba(59, 130, 246, 0.1)',
                                borderWidth: 3,
                                pointRadius: 6,
                                fill: false,
                                tension: 0.4
                            }, {
                                label: 'AI Predictions',
                                data: predictedData.map(item => item.total),
                                borderColor: '#EF4444',
                                backgroundColor: 'rgba(239, 68, 68, 0.1)',
                                borderWidth: 3,
                                borderDash: [10, 5],
                                pointRadius: 6,
                                fill: false,
                                tension: 0.4
                            }]
                        },
                        options: {
                            responsive: true,
                            maintainAspectRatio: false,
                            plugins: {
                                legend: {
                                    position: 'top',
                                    labels: { usePointStyle: true, padding: 20 }
                                },
                                tooltip: {
                                    backgroundColor: '#1F2937',
                                    titleColor: '#FFFFFF',
                                    bodyColor: '#FFFFFF',
                                    callbacks: {
                                        label: function(context) {
                                            return context.dataset.label + ': ₹' + context.parsed.y.toLocaleString();
                                        }
                                    }
                                }
                            },
                            scales: {
                                x: { grid: { display: false } },
                                y: {
                                    beginAtZero: true,
                                    grid: { color: '#F3F4F6' },
                                    ticks: {
                                        callback: function(value) {
                                            return '₹' + value.toLocaleString();
                                        }
                                    }
                                }
                            }
                        }
                    });
                }
            }
        });
        {% endif %}

        // Add fade-in animation on scroll
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);

        document.querySelectorAll('.fade-in').forEach(el => {
            el.style.opacity = '0';
            el.style.transform = 'translateY(20px)';
            el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
            observer.observe(el);
        });

        // Mobile sidebar toggle
        function toggleSidebar() {
            document.querySelector('.sidebar').classList.toggle('open');
        }
        
        // Month selector functionality
        function changeMonth(selectedMonth) {
            const currentUrl = new URL(window.location);
            currentUrl.searchParams.set('month', selectedMonth);
            window.location.href = currentUrl.toString();
        }
    </script>
</body>
</html>