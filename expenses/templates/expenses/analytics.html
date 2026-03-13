{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Analytics - BudgetWise</title>
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
                    <h1>Analytics</h1>
                    <p class="subtitle">Detailed spending insights</p>
                </div>
            </header>

            <!-- Summary Cards -->
            <div class="summary-grid">
                <div class="summary-card">
                    <div class="card-icon blue">💰</div>
                    <div class="card-content">
                        <div class="card-label">Total Expenses</div>
                        <div class="card-value">?{{ total_expenses|floatformat:2 }}</div>
                        <div class="card-subtitle">This month</div>
                    </div>
                </div>

                <div class="summary-card">
                    <div class="card-icon green">📝</div>
                    <div class="card-content">
                        <div class="card-label">Transactions</div>
                        <div class="card-value">{{ transaction_count }}</div>
                        <div class="card-subtitle">Total entries</div>
                    </div>
                </div>

                <div class="summary-card">
                    <div class="card-icon purple">💳</div>
                    <div class="card-content">
                        <div class="card-label">Budget</div>
                        <div class="card-value">?{{ budget_status.budget|floatformat:2 }}</div>
                        <div class="card-subtitle">Monthly limit</div>
                    </div>
                </div>

                <div class="summary-card">
                    <div class="card-icon {% if budget_status.remaining < 0 %}red{% else %}green{% endif %}">
                        💵
                    </div>
                    <div class="card-content">
                        <div class="card-label">Remaining</div>
                        <div class="card-value {% if budget_status.remaining < 0 %}negative{% endif %}">
                            ?{{ budget_status.remaining|floatformat:2 }}
                        </div>
                        <div class="card-subtitle">Available</div>
                    </div>
                </div>
            </div>

            <!-- Charts -->
            <div class="charts-grid-full">
                <div class="chart-card-large">
                    <div class="chart-header">
                        <h3>Spending Trend</h3>
                        <span class="chart-subtitle">Last 30 days</span>
                    </div>
                    <div class="chart-container-large">
                        <canvas id="trendChart"></canvas>
                    </div>
                </div>
            </div>

            <!-- Category Breakdown Table -->
            <div class="table-card">
                <h3 class="card-title">Category Breakdown</h3>
                {% if category_breakdown %}
                <div class="table-responsive">
                    <table class="analytics-table">
                        <thead>
                            <tr>
                                <th>Category</th>
                                <th>Transactions</th>
                                <th>Total Amount</th>
                                <th>Percentage</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for item in category_breakdown %}
                            <tr>
                                <td>
                                    <span class="category-badge">{{ item.category }}</span>
                                </td>
                                <td>{{ item.count }}</td>
                                <td class="amount-cell">?{{ item.total|floatformat:2 }}</td>
                                <td>
                                    <div class="percentage-bar">
                                        <div class="percentage-fill" style="width: {% widthratio item.total total_expenses 100 %}%"></div>
                                        <span class="percentage-text">{% widthratio item.total total_expenses 100 %}%</span>
                                    </div>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
                {% else %}
                <div class="empty-state">
                    <p>No expense data available for analysis.</p>
                </div>
                {% endif %}
            </div>
        </main>
    </div>

    <script>
        // Spending Trend Chart
        fetch('{% url "expenses:trend_chart" %}')
            .then(response => response.json())
            .then(data => {
                const ctx = document.getElementById('trendChart').getContext('2d');
                new Chart(ctx, {
                    type: 'line',
                    data: {
                        labels: data.labels,
                        datasets: [{
                            label: 'Daily Spending',
                            data: data.data,
                            borderColor: '#4f46e5',
                            backgroundColor: 'rgba(79, 70, 229, 0.1)',
                            borderWidth: 3,
                            fill: true,
                            tension: 0.4,
                            pointRadius: 4,
                            pointHoverRadius: 6
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: true,
                        plugins: {
                            legend: { display: false },
                            tooltip: {
                                callbacks: {
                                    label: function(context) {
                                        return '?' + context.parsed.y.toFixed(2);
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
    </script>
</body>
</html>

