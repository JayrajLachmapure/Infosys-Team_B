{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI Financial Insights - BudgetWise</title>
    <link rel="stylesheet" href="{% static 'css/modern-dashboard.css' %}">
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
</head>
<body>
    <div class="dashboard-layout">
        <!-- Sidebar -->
        {% include 'expenses/partials/sidebar.html' %}

        <!-- Main Content -->
        <main class="main-content">
            <header class="top-bar">
                <div class="top-bar-left">
                    <h1>🤖 AI Financial Insights</h1>
                    <p class="subtitle">Powered by Machine Learning</p>
                </div>
                <div class="top-bar-right">
                    <a href="{% url 'expenses:dashboard' %}" class="btn btn-secondary">← Back to Dashboard</a>
                </div>
            </header>

            <!-- AI Prediction Section -->
            <div class="ai-section">
                <h2 class="section-title">📊 Expense Forecast</h2>
                
                {% if prediction.success %}
                <div class="prediction-grid">
                    <div class="prediction-card main">
                        <div class="prediction-icon">🔮</div>
                        <div class="prediction-content">
                            <div class="prediction-label">Predicted Next Month</div>
                            <div class="prediction-value">?{{ prediction.predicted_amount|floatformat:2 }}</div>
                            <div class="prediction-meta">
                                <span class="confidence-badge">{{ prediction.confidence|floatformat:1 }}% confidence</span>
                                <span class="trend-badge {{ prediction.trend }}">{{ prediction.trend|title }}</span>
                            </div>
                        </div>
                    </div>

                    <div class="prediction-card">
                        <div class="card-icon-small">📈</div>
                        <div class="card-content-small">
                            <div class="card-label-small">Data Points</div>
                            <div class="card-value-medium">{{ prediction.data_points }} months</div>
                        </div>
                    </div>

                    <div class="prediction-card">
                        <div class="card-icon-small">🎯</div>
                        <div class="card-content-small">
                            <div class="card-label-small">Trend</div>
                            <div class="card-value-medium">{{ prediction.trend|title }}</div>
                        </div>
                    </div>
                </div>

                <!-- Forecast Chart -->
                <div class="chart-card-ai">
                    <div class="chart-header">
                        <h3>Expense Forecast Chart</h3>
                        <span class="chart-subtitle">Historical data + AI prediction</span>
                    </div>
                    <div class="chart-container-large">
                        <canvas id="forecastChart"></canvas>
                    </div>
                </div>
                {% else %}
                <div class="alert alert-info">
                    <strong>ℹ️ {{ prediction.message }}</strong>
                    <p>Keep tracking your expenses to enable AI predictions. We need at least 3 months of data.</p>
                </div>
                {% endif %}
            </div>

            <!-- AI Insights Section -->
            <div class="ai-section">
                <h2 class="section-title">💡 Financial Insights</h2>

                <!-- Overspending Alert -->
                <div class="insight-card {% if insights.overspending_alert.is_overspending %}alert-warning{% else %}alert-success{% endif %}">
                    <div class="insight-icon">
                        {% if insights.overspending_alert.is_overspending %}⚠️{% else %}✅{% endif %}
                    </div>
                    <div class="insight-content">
                        <h3>Spending Analysis</h3>
                        <p class="insight-message">{{ insights.overspending_alert.message }}</p>
                        <div class="insight-stats">
                            <div class="stat-item-small">
                                <span class="stat-label-small">Current Month</span>
                                <span class="stat-value-small">?{{ insights.overspending_alert.current_spending|floatformat:2 }}</span>
                            </div>
                            <div class="stat-item-small">
                                <span class="stat-label-small">Average</span>
                                <span class="stat-value-small">?{{ insights.overspending_alert.average_spending|floatformat:2 }}</span>
                            </div>
                            <div class="stat-item-small">
                                <span class="stat-label-small">Difference</span>
                                <span class="stat-value-small {% if insights.overspending_alert.percentage_above_average > 0 %}negative{% else %}positive{% endif %}">
                                    {{ insights.overspending_alert.percentage_above_average|floatformat:1 }}%
                                </span>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Insights Grid -->
                <div class="insights-grid">
                    <!-- Highest Category -->
                    <div class="insight-card-small">
                        <div class="insight-header-small">
                            <span class="insight-icon-small">🏆</span>
                            <h4>Top Category</h4>
                        </div>
                        <p class="insight-text">{{ insights.highest_category.message }}</p>
                        <div class="insight-value-large">{{ insights.highest_category.category }}</div>
                        <div class="insight-subtext">?{{ insights.highest_category.amount|floatformat:2 }} ({{ insights.highest_category.count }} transactions)</div>
                    </div>

                    <!-- Spending Change -->
                    <div class="insight-card-small">
                        <div class="insight-header-small">
                            <span class="insight-icon-small">
                                {% if insights.spending_change.direction == 'increased' %}📈
                                {% elif insights.spending_change.direction == 'decreased' %}📉
                                {% else %}➡️{% endif %}
                            </span>
                            <h4>Monthly Change</h4>
                        </div>
                        <p class="insight-text">{{ insights.spending_change.message }}</p>
                        <div class="insight-value-large {% if insights.spending_change.change_percentage > 0 %}negative{% else %}positive{% endif %}">
                            {{ insights.spending_change.change_percentage|floatformat:1 }}%
                        </div>
                        <div class="insight-subtext">
                            ?{{ insights.spending_change.change_amount|floatformat:2 }} change
                        </div>
                    </div>

                    <!-- Budget Status -->
                    <div class="insight-card-small">
                        <div class="insight-header-small">
                            <span class="insight-icon-small">💳</span>
                            <h4>Budget Status</h4>
                        </div>
                        {% if insights.budget_status.budget > 0 %}
                        <div class="budget-circle">
                            <svg viewBox="0 0 36 36" class="circular-chart">
                                <path class="circle-bg" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"/>
                                <path class="circle" stroke-dasharray="{{ insights.budget_status.percentage }}, 100" d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"/>
                                <text x="18" y="20.35" class="percentage">{{ insights.budget_status.percentage|floatformat:0 }}%</text>
                            </svg>
                        </div>
                        <div class="insight-subtext">
                            ?{{ insights.budget_status.remaining|floatformat:2 }} remaining
                        </div>
                        {% else %}
                        <p class="insight-text">No budget set for this month.</p>
                        <a href="{% url 'expenses:dashboard' %}" class="btn btn-primary btn-small">Set Budget</a>
                        {% endif %}
                    </div>
                </div>
            </div>

            <!-- Savings Advice Section -->
            <div class="ai-section">
                <h2 class="section-title">💰 Savings Recommendations</h2>
                <div class="advice-grid">
                    {% for advice in insights.savings_advice %}
                    <div class="advice-card {{ advice.type }}">
                        <span class="advice-icon">{{ advice.icon }}</span>
                        <p class="advice-text">{{ advice.message }}</p>
                    </div>
                    {% endfor %}
                </div>
            </div>
        </main>
    </div>

    <script>
        // Forecast Chart
        {% if prediction.success %}
        fetch('{% url "ai_engine:forecast_chart" %}')
            .then(response => response.json())
            .then(data => {
                if (!data.success) return;

                const ctx = document.getElementById('forecastChart').getContext('2d');
                
                // Combine historical and prediction data
                const labels = [...data.historical_labels];
                const historicalData = [...data.historical_data];
                const predictionData = new Array(data.historical_data.length).fill(null);
                
                if (data.prediction_label && data.prediction_value) {
                    labels.push(data.prediction_label);
                    predictionData.push(data.prediction_value);
                }
                
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: labels,
                        datasets: [
                            {
                                label: 'Historical Expenses',
                                data: historicalData,
                                borderColor: '#4f46e5',
                                backgroundColor: 'rgba(79, 70, 229, 0.1)',
                                borderWidth: 3,
                                fill: true,
                                tension: 0.4,
                                pointRadius: 5,
                                pointHoverRadius: 7
                            },
                            {
                                label: 'AI Prediction',
                                data: predictionData,
                                borderColor: '#10b981',
                                backgroundColor: 'rgba(16, 185, 129, 0.1)',
                                borderWidth: 3,
                                borderDash: [10, 5],
                                fill: false,
                                tension: 0.4,
                                pointRadius: 7,
                                pointHoverRadius: 9,
                                pointStyle: 'star'
                            }
                        ]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: true,
                        plugins: {
                            legend: {
                                position: 'top',
                                labels: {
                                    padding: 20,
                                    font: { size: 13, weight: 'bold' }
                                }
                            },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        let label = context.dataset.label || '';
                                        if (label) {
                                            label += ': ';
                                        }
                                        label += '?' + context.parsed.y.toFixed(2);
                                        return label;
                                    }
                                }
                            }
                        },
                        scales: {
                            y: {
                                beginAtZero: true,
                                ticks: {
                                    callback: function(value) {
                                        return '?' + value;
                                    }
                                }
                            }
                        }
                    }
                });
            });
        {% endif %}
    </script>
</body>
</html>

