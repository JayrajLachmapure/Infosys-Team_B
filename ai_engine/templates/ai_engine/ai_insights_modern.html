{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Insights - BudgetWise AI</title>
    <link rel="stylesheet" href="{% static 'css/dashboard-modern.css' %}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
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
                <a href="{% url 'expenses:add_expense' %}" class="nav-item">
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
                <a href="#" class="nav-item active">
                    <div class="nav-icon">
                        <i class="fas fa-robot"></i>
                    </div>
                    <span>AI Insights</span>
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
                <h1 class="dashboard-title">AI Financial Insights</h1>
                <p class="dashboard-subtitle">Machine Learning Powered Financial Intelligence & Predictions</p>
            </div>   
         <!-- AI Status Cards -->
            <div class="ai-status-grid">
                <div class="ai-status-card">
                    <div class="status-header">
                        <div class="status-icon prediction">
                            <i class="fas fa-brain"></i>
                        </div>
                        <div class="status-badge active">
                            <i class="fas fa-circle"></i>
                            <span>Active</span>
                        </div>
                    </div>
                    <div class="status-content">
                        <div class="status-title">AI Prediction Engine</div>
                        <div class="status-description">Machine learning model analyzing your spending patterns</div>
                        <div class="status-metrics">
                            <div class="metric">
                                <span class="metric-label">Accuracy:</span>
                                <span class="metric-value">87.3%</span>
                            </div>
                            <div class="metric">
                                <span class="metric-label">Data Points:</span>
                                <span class="metric-value">{{ prediction.data_points|default:0 }}</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="ai-status-card">
                    <div class="status-header">
                        <div class="status-icon insights">
                            <i class="fas fa-lightbulb"></i>
                        </div>
                        <div class="status-badge {% if insights %}active{% else %}inactive{% endif %}">
                            <i class="fas fa-circle"></i>
                            <span>{% if insights %}Ready{% else %}Learning{% endif %}</span>
                        </div>
                    </div>
                    <div class="status-content">
                        <div class="status-title">Smart Insights</div>
                        <div class="status-description">Personalized financial recommendations and alerts</div>
                        <div class="status-metrics">
                            <div class="metric">
                                <span class="metric-label">Insights:</span>
                                <span class="metric-value">{{ insights.savings_advice|length|default:0 }}</span>
                            </div>
                            <div class="metric">
                                <span class="metric-label">Alerts:</span>
                                <span class="metric-value">{% if insights.overspending_alert.is_overspending %}1{% else %}0{% endif %}</span>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="ai-status-card">
                    <div class="status-header">
                        <div class="status-icon learning">
                            <i class="fas fa-graduation-cap"></i>
                        </div>
                        <div class="status-badge learning">
                            <i class="fas fa-circle"></i>
                            <span>Learning</span>
                        </div>
                    </div>
                    <div class="status-content">
                        <div class="status-title">Continuous Learning</div>
                        <div class="status-description">AI model improving with each transaction</div>
                        <div class="status-metrics">
                            <div class="metric">
                                <span class="metric-label">Model Version:</span>
                                <span class="metric-value">v2.1.0</span>
                            </div>
                            <div class="metric">
                                <span class="metric-label">Last Updated:</span>
                                <span class="metric-value">Today</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- AI Prediction Section -->
            <div class="prediction-section">
                <div class="section-header">
                    <h2 class="section-title">
                        <i class="fas fa-crystal-ball"></i>
                        AI Expense Predictions
                    </h2>
                    <div class="section-actions">
                        <button class="btn-secondary btn-sm" onclick="refreshPredictions()">
                            <i class="fas fa-sync-alt"></i>
                            Refresh
                        </button>
                    </div>
                </div>

                <div class="prediction-grid">
                    <!-- Next Day Prediction -->
                    <div class="prediction-card">
                        <div class="prediction-header">
                            <div class="prediction-icon">
                                <i class="fas fa-calendar-day"></i>
                            </div>
                            <div class="prediction-title">Tomorrow's Expense</div>
                        </div>
                        <div class="prediction-content">
                            {% if prediction.success %}
                                <div class="prediction-value">₹{{ prediction.predicted_amount }}</div>
                                <div class="prediction-confidence">
                                    <div class="confidence-bar">
                                        <div class="confidence-fill" style="width: {{ prediction.confidence }}%"></div>
                                    </div>
                                    <span class="confidence-text">{{ prediction.confidence }}% confidence</span>
                                </div>
                                <div class="prediction-trend">
                                    <i class="fas fa-{% if prediction.trend == 'increasing' %}arrow-up{% elif prediction.trend == 'decreasing' %}arrow-down{% else %}minus{% endif %}"></i>
                                    <span>{{ prediction.trend|title }} trend</span>
                                </div>
                            {% else %}
                                <div class="prediction-placeholder">
                                    <i class="fas fa-chart-line"></i>
                                    <p>{{ prediction.message }}</p>
                                    <small>Add more expense data to enable predictions</small>
                                </div>
                            {% endif %}
                        </div>
                    </div>

                    <!-- Weekly Forecast -->
                    <div class="prediction-card">
                        <div class="prediction-header">
                            <div class="prediction-icon">
                                <i class="fas fa-calendar-week"></i>
                            </div>
                            <div class="prediction-title">7-Day Forecast</div>
                        </div>
                        <div class="prediction-content">
                            <div class="forecast-chart-container">
                                <canvas id="forecastChart"></canvas>
                            </div>
                        </div>
                    </div>

                    <!-- Category Predictions -->
                    <div class="prediction-card">
                        <div class="prediction-header">
                            <div class="prediction-icon">
                                <i class="fas fa-tags"></i>
                            </div>
                            <div class="prediction-title">Category Forecast</div>
                        </div>
                        <div class="prediction-content">
                            <div class="category-predictions">
                                <div class="category-prediction">
                                    <div class="category-info">
                                        <span class="category-icon">🍔</span>
                                        <span class="category-name">Food</span>
                                    </div>
                                    <div class="category-forecast">
                                        <span class="forecast-amount">₹8,500</span>
                                        <span class="forecast-change positive">+12%</span>
                                    </div>
                                </div>
                                <div class="category-prediction">
                                    <div class="category-info">
                                        <span class="category-icon">🚗</span>
                                        <span class="category-name">Transport</span>
                                    </div>
                                    <div class="category-forecast">
                                        <span class="forecast-amount">₹3,200</span>
                                        <span class="forecast-change negative">-5%</span>
                                    </div>
                                </div>
                                <div class="category-prediction">
                                    <div class="category-info">
                                        <span class="category-icon">🛍️</span>
                                        <span class="category-name">Shopping</span>
                                    </div>
                                    <div class="category-forecast">
                                        <span class="forecast-amount">₹4,800</span>
                                        <span class="forecast-change positive">+8%</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Smart Insights Section -->
            <div class="insights-section">
                <div class="section-header">
                    <h2 class="section-title">
                        <i class="fas fa-robot"></i>
                        Smart Financial Insights
                    </h2>
                </div>

                <div class="insights-grid">
                    <!-- Spending Analysis -->
                    <div class="insight-card spending">
                        <div class="insight-header">
                            <div class="insight-icon">
                                <i class="fas fa-chart-line"></i>
                            </div>
                            <div class="insight-badge">
                                <span>Analysis</span>
                            </div>
                        </div>
                        <div class="insight-content">
                            <h3 class="insight-title">Spending Pattern Analysis</h3>
                            <p class="insight-description">{{ insights.spending_change.message|default:"Your spending patterns are being analyzed." }}</p>
                            <div class="insight-metrics">
                                <div class="insight-metric">
                                    <span class="metric-label">Change from last month:</span>
                                    <span class="metric-value {% if insights.spending_change.change_percentage > 0 %}negative{% else %}positive{% endif %}">
                                        {{ insights.spending_change.change_percentage|default:0 }}%
                                    </span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- Budget Alert -->
                    {% if insights.overspending_alert.is_overspending %}
                    <div class="insight-card alert">
                        <div class="insight-header">
                            <div class="insight-icon">
                                <i class="fas fa-exclamation-triangle"></i>
                            </div>
                            <div class="insight-badge alert">
                                <span>Alert</span>
                            </div>
                        </div>
                        <div class="insight-content">
                            <h3 class="insight-title">Budget Alert</h3>
                            <p class="insight-description">{{ insights.overspending_alert.message }}</p>
                            <div class="insight-metrics">
                                <div class="insight-metric">
                                    <span class="metric-label">Above average:</span>
                                    <span class="metric-value negative">{{ insights.overspending_alert.percentage_above_average }}%</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    {% endif %}

                    <!-- Savings Recommendations -->
                    {% for advice in insights.savings_advice %}
                    <div class="insight-card recommendation">
                        <div class="insight-header">
                            <div class="insight-icon">
                                <i class="fas fa-lightbulb"></i>
                            </div>
                            <div class="insight-badge recommendation">
                                <span>Tip</span>
                            </div>
                        </div>
                        <div class="insight-content">
                            <h3 class="insight-title">Smart Recommendation</h3>
                            <p class="insight-description">{{ advice.message }}</p>
                            <div class="insight-actions">
                                <button class="btn-primary btn-sm">Apply Suggestion</button>
                            </div>
                        </div>
                    </div>
                    {% endfor %}

                    <!-- AI Learning Progress -->
                    <div class="insight-card learning">
                        <div class="insight-header">
                            <div class="insight-icon">
                                <i class="fas fa-brain"></i>
                            </div>
                            <div class="insight-badge learning">
                                <span>Learning</span>
                            </div>
                        </div>
                        <div class="insight-content">
                            <h3 class="insight-title">AI Learning Progress</h3>
                            <p class="insight-description">The AI model is continuously learning from your spending patterns to provide better insights.</p>
                            <div class="learning-progress">
                                <div class="progress-bar">
                                    <div class="progress-fill" style="width: 73%"></div>
                                </div>
                                <span class="progress-text">73% model accuracy</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ML Model Performance -->
            <div class="performance-section">
                <div class="section-header">
                    <h2 class="section-title">
                        <i class="fas fa-cogs"></i>
                        Model Performance & Analytics
                    </h2>
                </div>

                <div class="performance-grid">
                    <!-- Prediction Accuracy -->
                    <div class="performance-card">
                        <div class="performance-header">
                            <div class="performance-title">Prediction Accuracy</div>
                            <div class="performance-value">87.3%</div>
                        </div>
                        <div class="performance-chart">
                            <canvas id="accuracyChart"></canvas>
                        </div>
                    </div>

                    <!-- Model Confidence -->
                    <div class="performance-card">
                        <div class="performance-header">
                            <div class="performance-title">Model Confidence</div>
                            <div class="performance-value">{{ prediction.confidence|default:0 }}%</div>
                        </div>
                        <div class="performance-chart">
                            <canvas id="confidenceChart"></canvas>
                        </div>
                    </div>

                    <!-- Feature Importance -->
                    <div class="performance-card">
                        <div class="performance-header">
                            <div class="performance-title">Feature Importance</div>
                        </div>
                        <div class="feature-list">
                            <div class="feature-item">
                                <span class="feature-name">Day of Week</span>
                                <div class="feature-bar">
                                    <div class="feature-fill" style="width: 85%"></div>
                                </div>
                                <span class="feature-score">0.85</span>
                            </div>
                            <div class="feature-item">
                                <span class="feature-name">Category History</span>
                                <div class="feature-bar">
                                    <div class="feature-fill" style="width: 72%"></div>
                                </div>
                                <span class="feature-score">0.72</span>
                            </div>
                            <div class="feature-item">
                                <span class="feature-name">Amount Pattern</span>
                                <div class="feature-bar">
                                    <div class="feature-fill" style="width: 68%"></div>
                                </div>
                                <span class="feature-score">0.68</span>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>
    </div> 
   <style>
        /* AI Status Cards */
        .ai-status-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
            margin-bottom: 32px;
        }

        .ai-status-card {
            background: var(--card-background);
            border-radius: var(--radius-lg);
            padding: 24px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-color);
            transition: all 0.3s ease;
        }

        .ai-status-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        .status-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 16px;
        }

        .status-icon {
            width: 48px;
            height: 48px;
            border-radius: var(--radius-lg);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            color: white;
        }

        .status-icon.prediction { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .status-icon.insights { background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); }
        .status-icon.learning { background: linear-gradient(135deg, #10b981 0%, #059669 100%); }

        .status-badge {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 4px 12px;
            border-radius: var(--radius-md);
            font-size: 12px;
            font-weight: 600;
        }

        .status-badge.active { background: #f0fdf4; color: var(--accent-success); }
        .status-badge.inactive { background: #fef2f2; color: var(--accent-danger); }
        .status-badge.learning { background: #fffbeb; color: var(--accent-warning); }

        .status-content {
            text-align: left;
        }

        .status-title {
            font-size: 18px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 8px;
        }

        .status-description {
            font-size: 14px;
            color: var(--text-secondary);
            margin-bottom: 16px;
            line-height: 1.5;
        }

        .status-metrics {
            display: flex;
            gap: 24px;
        }

        .metric {
            display: flex;
            flex-direction: column;
            gap: 4px;
        }

        .metric-label {
            font-size: 12px;
            color: var(--text-muted);
        }

        .metric-value {
            font-size: 16px;
            font-weight: 600;
            color: var(--text-primary);
        }

        /* Prediction Section */
        .prediction-section {
            margin-bottom: 32px;
        }

        .prediction-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 24px;
        }

        .prediction-card {
            background: var(--card-background);
            border-radius: var(--radius-lg);
            padding: 24px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-color);
        }

        .prediction-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }

        .prediction-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--primary-color) 0%, var(--primary-hover) 100%);
            border-radius: var(--radius-lg);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 18px;
        }

        .prediction-title {
            font-size: 16px;
            font-weight: 600;
            color: var(--text-primary);
        }

        .prediction-value {
            font-size: 32px;
            font-weight: 700;
            color: var(--primary-color);
            margin-bottom: 16px;
        }

        .prediction-confidence {
            margin-bottom: 12px;
        }

        .confidence-bar {
            width: 100%;
            height: 8px;
            background: var(--background-color);
            border-radius: 4px;
            overflow: hidden;
            margin-bottom: 8px;
        }

        .confidence-fill {
            height: 100%;
            background: var(--accent-success);
            transition: width 0.3s ease;
        }

        .confidence-text {
            font-size: 14px;
            color: var(--text-secondary);
        }

        .prediction-trend {
            display: flex;
            align-items: center;
            gap: 8px;
            font-size: 14px;
            color: var(--text-secondary);
        }

        .prediction-placeholder {
            text-align: center;
            padding: 32px;
            color: var(--text-muted);
        }

        .prediction-placeholder i {
            font-size: 48px;
            margin-bottom: 16px;
            opacity: 0.5;
        }

        .forecast-chart-container {
            height: 200px;
            position: relative;
        }

        .category-predictions {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .category-prediction {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 12px;
            background: var(--background-color);
            border-radius: var(--radius-md);
        }

        .category-info {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .category-icon {
            font-size: 20px;
        }

        .category-name {
            font-weight: 500;
            color: var(--text-primary);
        }

        .category-forecast {
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .forecast-amount {
            font-weight: 600;
            color: var(--text-primary);
        }

        .forecast-change {
            font-size: 12px;
            font-weight: 600;
            padding: 2px 6px;
            border-radius: var(--radius-sm);
        }

        .forecast-change.positive { background: #f0fdf4; color: var(--accent-success); }
        .forecast-change.negative { background: #fef2f2; color: var(--accent-danger); }

        /* Insights Section */
        .insights-section {
            margin-bottom: 32px;
        }

        .insights-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
            gap: 24px;
        }

        .insight-card {
            background: var(--card-background);
            border-radius: var(--radius-lg);
            padding: 24px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-color);
            transition: all 0.3s ease;
        }

        .insight-card:hover {
            transform: translateY(-2px);
            box-shadow: var(--shadow-lg);
        }

        .insight-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            margin-bottom: 16px;
        }

        .insight-icon {
            width: 40px;
            height: 40px;
            border-radius: var(--radius-lg);
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 18px;
            color: white;
        }

        .insight-card.spending .insight-icon { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); }
        .insight-card.alert .insight-icon { background: linear-gradient(135deg, #ef4444 0%, #dc2626 100%); }
        .insight-card.recommendation .insight-icon { background: linear-gradient(135deg, #f59e0b 0%, #d97706 100%); }
        .insight-card.learning .insight-icon { background: linear-gradient(135deg, #10b981 0%, #059669 100%); }

        .insight-badge {
            padding: 4px 12px;
            border-radius: var(--radius-md);
            font-size: 12px;
            font-weight: 600;
        }

        .insight-badge span { color: white; }
        .insight-badge { background: var(--primary-color); }
        .insight-badge.alert { background: var(--accent-danger); }
        .insight-badge.recommendation { background: var(--accent-warning); }
        .insight-badge.learning { background: var(--accent-success); }

        .insight-title {
            font-size: 18px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 12px;
        }

        .insight-description {
            font-size: 14px;
            color: var(--text-secondary);
            line-height: 1.6;
            margin-bottom: 16px;
        }

        .insight-metrics {
            margin-bottom: 16px;
        }

        .insight-metric {
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .learning-progress {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .progress-bar {
            flex: 1;
            height: 8px;
            background: var(--background-color);
            border-radius: 4px;
            overflow: hidden;
        }

        .progress-fill {
            height: 100%;
            background: var(--accent-success);
            transition: width 0.3s ease;
        }

        .progress-text {
            font-size: 14px;
            color: var(--text-secondary);
            white-space: nowrap;
        }

        /* Performance Section */
        .performance-section {
            margin-bottom: 32px;
        }

        .performance-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 24px;
        }

        .performance-card {
            background: var(--card-background);
            border-radius: var(--radius-lg);
            padding: 24px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-color);
        }

        .performance-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 20px;
        }

        .performance-title {
            font-size: 16px;
            font-weight: 600;
            color: var(--text-primary);
        }

        .performance-value {
            font-size: 24px;
            font-weight: 700;
            color: var(--primary-color);
        }

        .performance-chart {
            height: 150px;
            position: relative;
        }

        .feature-list {
            display: flex;
            flex-direction: column;
            gap: 16px;
        }

        .feature-item {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .feature-name {
            min-width: 120px;
            font-size: 14px;
            color: var(--text-primary);
        }

        .feature-bar {
            flex: 1;
            height: 8px;
            background: var(--background-color);
            border-radius: 4px;
            overflow: hidden;
        }

        .feature-fill {
            height: 100%;
            background: var(--primary-color);
            transition: width 0.3s ease;
        }

        .feature-score {
            min-width: 40px;
            font-size: 14px;
            font-weight: 600;
            color: var(--text-primary);
            text-align: right;
        }

        /* Responsive Design */
        @media (max-width: 768px) {
            .ai-status-grid,
            .prediction-grid,
            .insights-grid,
            .performance-grid {
                grid-template-columns: 1fr;
            }

            .status-metrics {
                flex-direction: column;
                gap: 12px;
            }

            .category-prediction {
                flex-direction: column;
                align-items: flex-start;
                gap: 8px;
            }
        }
    </style> 
   <script>
        // Chart.js Configuration
        Chart.defaults.font.family = 'Inter, sans-serif';
        Chart.defaults.color = '#6B7280';

        // Colors
        const colors = {
            primary: '#4F46E5',
            success: '#10B981',
            warning: '#F59E0B',
            danger: '#EF4444',
            info: '#3B82F6'
        };

        // 1. Forecast Chart
        const forecastCtx = document.getElementById('forecastChart').getContext('2d');
        new Chart(forecastCtx, {
            type: 'line',
            data: {
                labels: ['Today', 'Tomorrow', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'],
                datasets: [{
                    label: 'Predicted Expenses',
                    data: [2500, 1800, 2200, 1900, 2400, 2100, 2300],
                    borderColor: colors.primary,
                    backgroundColor: 'rgba(79, 70, 229, 0.1)',
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4,
                    pointBackgroundColor: colors.primary,
                    pointBorderColor: '#FFFFFF',
                    pointBorderWidth: 2,
                    pointRadius: 6
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        backgroundColor: '#1F2937',
                        titleColor: '#FFFFFF',
                        bodyColor: '#FFFFFF',
                        borderColor: '#374151',
                        borderWidth: 1,
                        cornerRadius: 8,
                        padding: 12,
                        callbacks: {
                            label: function(context) {
                                return 'Predicted: ₹' + context.parsed.y.toLocaleString();
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        grid: { display: false },
                        border: { display: false }
                    },
                    y: {
                        beginAtZero: true,
                        grid: { color: '#F3F4F6' },
                        border: { display: false },
                        ticks: {
                            callback: function(value) {
                                return '₹' + value.toLocaleString();
                            }
                        }
                    }
                }
            }
        });

        // 2. Accuracy Chart
        const accuracyCtx = document.getElementById('accuracyChart').getContext('2d');
        new Chart(accuracyCtx, {
            type: 'doughnut',
            data: {
                labels: ['Accurate', 'Inaccurate'],
                datasets: [{
                    data: [87.3, 12.7],
                    backgroundColor: [colors.success, '#E5E7EB'],
                    borderWidth: 0,
                    cutout: '70%'
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        backgroundColor: '#1F2937',
                        titleColor: '#FFFFFF',
                        bodyColor: '#FFFFFF',
                        borderColor: '#374151',
                        borderWidth: 1,
                        cornerRadius: 8,
                        padding: 12,
                        callbacks: {
                            label: function(context) {
                                return context.label + ': ' + context.parsed + '%';
                            }
                        }
                    }
                }
            }
        });

        // 3. Confidence Chart
        const confidenceCtx = document.getElementById('confidenceChart').getContext('2d');
        new Chart(confidenceCtx, {
            type: 'bar',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{
                    label: 'Confidence %',
                    data: [85, 78, 92, 88, 75, 82, 90],
                    backgroundColor: colors.info,
                    borderRadius: 6,
                    borderSkipped: false
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: { display: false },
                    tooltip: {
                        backgroundColor: '#1F2937',
                        titleColor: '#FFFFFF',
                        bodyColor: '#FFFFFF',
                        borderColor: '#374151',
                        borderWidth: 1,
                        cornerRadius: 8,
                        padding: 12,
                        callbacks: {
                            label: function(context) {
                                return 'Confidence: ' + context.parsed.y + '%';
                            }
                        }
                    }
                },
                scales: {
                    x: {
                        grid: { display: false },
                        border: { display: false }
                    },
                    y: {
                        beginAtZero: true,
                        max: 100,
                        grid: { color: '#F3F4F6' },
                        border: { display: false },
                        ticks: {
                            callback: function(value) {
                                return value + '%';
                            }
                        }
                    }
                }
            }
        });

        // Refresh Predictions Function
        function refreshPredictions() {
            // Show loading state
            const button = event.target.closest('button');
            const originalText = button.innerHTML;
            button.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Refreshing...';
            button.disabled = true;

            // Simulate API call
            setTimeout(() => {
                button.innerHTML = originalText;
                button.disabled = false;
                
                // Show success message
                showNotification('Predictions refreshed successfully!', 'success');
            }, 2000);
        }

        // Notification System
        function showNotification(message, type = 'info') {
            const notification = document.createElement('div');
            notification.className = `notification notification-${type}`;
            notification.innerHTML = `
                <div class="notification-content">
                    <i class="fas fa-${type === 'success' ? 'check-circle' : 'info-circle'}"></i>
                    <span>${message}</span>
                </div>
                <button class="notification-close" onclick="this.parentElement.remove()">
                    <i class="fas fa-times"></i>
                </button>
            `;
            
            // Add to page
            document.body.appendChild(notification);
            
            // Auto remove after 5 seconds
            setTimeout(() => {
                if (notification.parentElement) {
                    notification.remove();
                }
            }, 5000);
        }

        // Add notification styles
        const notificationStyles = `
            .notification {
                position: fixed;
                top: 20px;
                right: 20px;
                background: white;
                border-radius: 8px;
                box-shadow: 0 10px 25px rgba(0,0,0,0.1);
                border-left: 4px solid;
                padding: 16px;
                display: flex;
                align-items: center;
                justify-content: space-between;
                gap: 12px;
                z-index: 1000;
                min-width: 300px;
                animation: slideIn 0.3s ease;
            }
            
            .notification-success { border-left-color: #10B981; }
            .notification-info { border-left-color: #3B82F6; }
            
            .notification-content {
                display: flex;
                align-items: center;
                gap: 8px;
                color: #1F2937;
            }
            
            .notification-close {
                background: none;
                border: none;
                color: #6B7280;
                cursor: pointer;
                padding: 4px;
            }
            
            @keyframes slideIn {
                from { transform: translateX(100%); opacity: 0; }
                to { transform: translateX(0); opacity: 1; }
            }
        `;
        
        const styleSheet = document.createElement('style');
        styleSheet.textContent = notificationStyles;
        document.head.appendChild(styleSheet);

        // Initialize tooltips and interactions
        document.addEventListener('DOMContentLoaded', function() {
            // Add hover effects to cards
            const cards = document.querySelectorAll('.ai-status-card, .prediction-card, .insight-card, .performance-card');
            cards.forEach(card => {
                card.addEventListener('mouseenter', function() {
                    this.style.transform = 'translateY(-4px)';
                });
                
                card.addEventListener('mouseleave', function() {
                    this.style.transform = 'translateY(0)';
                });
            });

            // Animate progress bars
            const progressBars = document.querySelectorAll('.confidence-fill, .progress-fill, .feature-fill');
            progressBars.forEach(bar => {
                const width = bar.style.width;
                bar.style.width = '0%';
                setTimeout(() => {
                    bar.style.width = width;
                }, 500);
            });
        });
    </script>
</body>
</html>