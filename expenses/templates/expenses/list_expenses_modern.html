{% load static %}
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>All Expenses - BudgetWise AI</title>
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
                <a href="{% url 'expenses:dashboard' %}{% if selected_month %}?month={{ selected_month }}{% endif %}" class="nav-item">
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
                <a href="{% url 'expenses:list_expenses' %}{% if selected_month %}?month={{ selected_month }}{% endif %}" class="nav-item active">
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
            <!-- Page Header -->
            <div class="dashboard-header">
                <h1 class="dashboard-title">All Expenses</h1>
                <p class="dashboard-subtitle">Manage and track all your expenses</p>
            </div>

            <!-- Filter Section -->
            <div class="filter-section">
                <div class="filter-card">
                    <div class="filter-header">
                        <div class="filter-icon">
                            <i class="fas fa-filter"></i>
                        </div>
                        <h3 class="filter-title">Filter & Search</h3>
                    </div>
                    
                    <form method="get" class="filter-form">
                        <div class="filter-grid">
                            <div class="form-group">
                                <label class="form-label">
                                    <i class="fas fa-tags"></i>
                                    Category
                                </label>
                                {{ filter_form.category }}
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">
                                    <i class="fas fa-calendar-alt"></i>
                                    Month
                                </label>
                                {{ filter_form.month }}
                            </div>
                            
                            <div class="form-group">
                                <label class="form-label">
                                    <i class="fas fa-search"></i>
                                    Search
                                </label>
                                {{ filter_form.search }}
                            </div>
                            
                            <div class="form-group">
                                <button type="submit" class="btn-primary">
                                    <i class="fas fa-search"></i>
                                    Filter
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>

            <!-- Summary Stats -->
            <div class="summary-grid">
                <div class="summary-card">
                    <div class="card-header">
                        <div class="card-icon expenses">
                            <i class="fas fa-calculator"></i>
                        </div>
                    </div>
                    <div class="card-content">
                        <div class="card-value">₹{{ total|floatformat:0 }}</div>
                        <div class="card-label">Total Amount</div>
                    </div>
                    <div class="card-footer">
                        <div class="card-trend neutral">
                            <i class="fas fa-list"></i>
                            <span>Filtered results</span>
                        </div>
                    </div>
                </div>

                <div class="summary-card">
                    <div class="card-header">
                        <div class="card-icon transactions">
                            <i class="fas fa-receipt"></i>
                        </div>
                    </div>
                    <div class="card-content">
                        <div class="card-value">{{ count }}</div>
                        <div class="card-label">Total Expenses</div>
                    </div>
                    <div class="card-footer">
                        <div class="card-trend neutral">
                            <i class="fas fa-hashtag"></i>
                            <span>Transactions</span>
                        </div>
                    </div>
                </div>

                <div class="summary-card">
                    <div class="card-header">
                        <div class="card-icon category">
                            <i class="fas fa-chart-pie"></i>
                        </div>
                    </div>
                    <div class="card-content">
                        <div class="card-value">₹{{ average|floatformat:0 }}</div>
                        <div class="card-label">Average Amount</div>
                    </div>
                    <div class="card-footer">
                        <div class="card-trend neutral">
                            <i class="fas fa-calculator"></i>
                            <span>Per transaction</span>
                        </div>
                    </div>
                </div>

                <div class="summary-card">
                    <div class="card-header">
                        <div class="card-icon savings">
                            <i class="fas fa-plus-circle"></i>
                        </div>
                    </div>
                    <div class="card-content">
                        <div class="card-value">
                            <a href="{% url 'expenses:add_expense' %}" class="add-expense-btn">
                                <i class="fas fa-plus"></i>
                            </a>
                        </div>
                        <div class="card-label">Add New Expense</div>
                    </div>
                    <div class="card-footer">
                        <div class="card-trend positive">
                            <i class="fas fa-arrow-right"></i>
                            <span>Quick action</span>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Expenses Table -->
            <div class="table-section">
                <div class="table-card">
                    <div class="table-header">
                        <div class="table-title">
                            <i class="fas fa-table"></i>
                            Expense Details
                        </div>
                        <div class="table-actions">
                            <button class="btn-secondary btn-sm" onclick="exportData()">
                                <i class="fas fa-download"></i>
                                Export
                            </button>
                        </div>
                    </div>
                    
                    <div class="table-container">
                        {% if page_obj %}
                        <table class="modern-table">
                            <thead>
                                <tr>
                                    <th>Date</th>
                                    <th>Category</th>
                                    <th>Description</th>
                                    <th>Amount</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                {% for expense in page_obj %}
                                <tr class="table-row">
                                    <td class="date-cell">
                                        <div class="date-display">
                                            <div class="date-day">{{ expense.date|date:"d" }}</div>
                                            <div class="date-month">{{ expense.date|date:"M Y" }}</div>
                                        </div>
                                    </td>
                                    <td class="category-cell">
                                        <div class="category-badge category-{{ expense.category|lower }}">
                                            <span class="category-icon">{{ expense.get_category_icon }}</span>
                                            <span class="category-name">{{ expense.category }}</span>
                                        </div>
                                    </td>
                                    <td class="description-cell">
                                        <div class="description-text">
                                            {{ expense.description|default:"No description" }}
                                        </div>
                                    </td>
                                    <td class="amount-cell">
                                        <div class="amount-display">
                                            <span class="currency">₹</span>
                                            <span class="amount">{{ expense.amount|floatformat:2 }}</span>
                                        </div>
                                    </td>
                                    <td class="actions-cell">
                                        <div class="action-buttons">
                                            <a href="{% url 'expenses:edit_expense' expense.id %}" class="btn-action btn-edit" title="Edit">
                                                <i class="fas fa-edit"></i>
                                            </a>
                                            <form method="post" action="{% url 'expenses:delete_expense' expense.id %}" class="delete-form" onsubmit="return confirm('Are you sure you want to delete this expense?')">
                                                {% csrf_token %}
                                                <input type="hidden" name="next" value="{% url 'expenses:list_expenses' %}">
                                                <button type="submit" class="btn-action btn-delete" title="Delete">
                                                    <i class="fas fa-trash"></i>
                                                </button>
                                            </form>
                                        </div>
                                    </td>
                                </tr>
                                {% endfor %}
                            </tbody>
                        </table>
                        {% else %}
                        <div class="empty-state">
                            <div class="empty-icon">
                                <i class="fas fa-receipt"></i>
                            </div>
                            <h3 class="empty-title">No Expenses Found</h3>
                            <p class="empty-message">Start tracking your expenses by adding your first transaction.</p>
                            <a href="{% url 'expenses:add_expense' %}" class="btn-primary">
                                <i class="fas fa-plus"></i>
                                Add First Expense
                            </a>
                        </div>
                        {% endif %}
                    </div>

                    <!-- Pagination -->
                    {% if page_obj.has_other_pages %}
                    <div class="pagination-container">
                        <div class="pagination">
                            {% if page_obj.has_previous %}
                                <a href="?page=1" class="page-btn">
                                    <i class="fas fa-angle-double-left"></i>
                                </a>
                                <a href="?page={{ page_obj.previous_page_number }}" class="page-btn">
                                    <i class="fas fa-angle-left"></i>
                                </a>
                            {% endif %}
                            
                            <span class="page-info">
                                Page {{ page_obj.number }} of {{ page_obj.paginator.num_pages }}
                            </span>
                            
                            {% if page_obj.has_next %}
                                <a href="?page={{ page_obj.next_page_number }}" class="page-btn">
                                    <i class="fas fa-angle-right"></i>
                                </a>
                                <a href="?page={{ page_obj.paginator.num_pages }}" class="page-btn">
                                    <i class="fas fa-angle-double-right"></i>
                                </a>
                            {% endif %}
                        </div>
                    </div>
                    {% endif %}
                </div>
            </div>
        </main>
    </div>

    <style>
        .filter-section {
            margin-bottom: 32px;
        }

        .filter-card {
            background: var(--card-background);
            border-radius: var(--radius-lg);
            padding: 24px;
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-color);
        }

        .filter-header {
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 20px;
        }

        .filter-icon {
            width: 40px;
            height: 40px;
            background: linear-gradient(135deg, var(--accent-info) 0%, #1d4ed8 100%);
            border-radius: var(--radius-lg);
            display: flex;
            align-items: center;
            justify-content: center;
            color: white;
            font-size: 18px;
        }

        .filter-title {
            font-size: 18px;
            font-weight: 600;
            color: var(--text-primary);
        }

        .filter-form {
            width: 100%;
        }

        .filter-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            align-items: end;
        }

        .add-expense-btn {
            display: flex;
            align-items: center;
            justify-content: center;
            width: 48px;
            height: 48px;
            background: var(--primary-color);
            color: white;
            border-radius: 50%;
            text-decoration: none;
            font-size: 20px;
            transition: all 0.2s ease;
        }

        .add-expense-btn:hover {
            background: var(--primary-hover);
            transform: scale(1.1);
        }

        .table-section {
            margin-bottom: 32px;
        }

        .table-card {
            background: var(--card-background);
            border-radius: var(--radius-lg);
            box-shadow: var(--shadow-md);
            border: 1px solid var(--border-color);
            overflow: hidden;
        }

        .table-header {
            display: flex;
            align-items: center;
            justify-content: space-between;
            padding: 24px;
            border-bottom: 1px solid var(--border-color);
        }

        .table-title {
            display: flex;
            align-items: center;
            gap: 12px;
            font-size: 18px;
            font-weight: 600;
            color: var(--text-primary);
        }

        .table-actions {
            display: flex;
            gap: 12px;
        }

        .btn-sm {
            padding: 8px 16px;
            font-size: 13px;
        }

        .table-container {
            overflow-x: auto;
        }

        .modern-table {
            width: 100%;
            border-collapse: collapse;
        }

        .modern-table th {
            background: var(--background-color);
            padding: 16px;
            text-align: left;
            font-weight: 600;
            color: var(--text-primary);
            font-size: 14px;
            border-bottom: 1px solid var(--border-color);
        }

        .table-row {
            transition: all 0.2s ease;
        }

        .table-row:hover {
            background: var(--background-color);
        }

        .modern-table td {
            padding: 16px;
            border-bottom: 1px solid var(--border-color);
            vertical-align: middle;
        }

        .date-display {
            display: flex;
            flex-direction: column;
            align-items: center;
            gap: 2px;
        }

        .date-day {
            font-size: 18px;
            font-weight: 700;
            color: var(--text-primary);
        }

        .date-month {
            font-size: 12px;
            color: var(--text-secondary);
        }

        .category-badge {
            display: flex;
            align-items: center;
            gap: 8px;
            padding: 6px 12px;
            border-radius: var(--radius-md);
            background: var(--background-color);
            border: 1px solid var(--border-color);
        }

        .category-icon {
            font-size: 16px;
        }

        .category-name {
            font-size: 13px;
            font-weight: 500;
        }

        .description-text {
            color: var(--text-secondary);
            font-size: 14px;
            max-width: 200px;
            overflow: hidden;
            text-overflow: ellipsis;
            white-space: nowrap;
        }

        .amount-display {
            display: flex;
            align-items: center;
            gap: 2px;
            font-weight: 600;
            color: var(--text-primary);
        }

        .currency {
            font-size: 14px;
            color: var(--text-secondary);
        }

        .amount {
            font-size: 16px;
        }

        .action-buttons {
            display: flex;
            gap: 8px;
        }

        .btn-action {
            width: 32px;
            height: 32px;
            border-radius: var(--radius-sm);
            border: none;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: all 0.2s ease;
            font-size: 14px;
        }

        .btn-edit {
            background: var(--accent-info);
            color: white;
        }

        .btn-edit:hover {
            background: #1d4ed8;
        }

        .btn-delete {
            background: var(--accent-danger);
            color: white;
        }

        .btn-delete:hover {
            background: #dc2626;
        }

        .delete-form {
            display: inline;
        }

        .empty-state {
            text-align: center;
            padding: 64px 32px;
        }

        .empty-icon {
            width: 80px;
            height: 80px;
            background: var(--background-color);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 24px;
            font-size: 32px;
            color: var(--text-muted);
        }

        .empty-title {
            font-size: 24px;
            font-weight: 600;
            color: var(--text-primary);
            margin-bottom: 12px;
        }

        .empty-message {
            font-size: 16px;
            color: var(--text-secondary);
            margin-bottom: 24px;
        }

        .pagination-container {
            padding: 24px;
            border-top: 1px solid var(--border-color);
            display: flex;
            justify-content: center;
        }

        .pagination {
            display: flex;
            align-items: center;
            gap: 12px;
        }

        .page-btn {
            width: 40px;
            height: 40px;
            border-radius: var(--radius-md);
            background: var(--background-color);
            border: 1px solid var(--border-color);
            display: flex;
            align-items: center;
            justify-content: center;
            text-decoration: none;
            color: var(--text-primary);
            transition: all 0.2s ease;
        }

        .page-btn:hover {
            background: var(--primary-color);
            color: white;
            border-color: var(--primary-color);
        }

        .page-info {
            padding: 0 16px;
            font-size: 14px;
            color: var(--text-secondary);
        }

        @media (max-width: 768px) {
            .filter-grid {
                grid-template-columns: 1fr;
            }

            .table-container {
                font-size: 14px;
            }

            .modern-table th,
            .modern-table td {
                padding: 12px 8px;
            }

            .description-text {
                max-width: 120px;
            }
        }
    </style>

    <script>
        function exportData() {
            // Simple CSV export functionality
            const table = document.querySelector('.modern-table');
            if (!table) return;
            
            let csv = [];
            const rows = table.querySelectorAll('tr');
            
            for (let i = 0; i < rows.length; i++) {
                const row = [];
                const cols = rows[i].querySelectorAll('td, th');
                
                for (let j = 0; j < cols.length - 1; j++) { // Exclude actions column
                    row.push(cols[j].innerText.replace(/,/g, ';'));
                }
                csv.push(row.join(','));
            }
            
            const csvFile = new Blob([csv.join('\n')], { type: 'text/csv' });
            const downloadLink = document.createElement('a');
            downloadLink.download = 'expenses.csv';
            downloadLink.href = window.URL.createObjectURL(csvFile);
            downloadLink.style.display = 'none';
            document.body.appendChild(downloadLink);
            downloadLink.click();
            document.body.removeChild(downloadLink);
        }
    </script>
</body>
</html>