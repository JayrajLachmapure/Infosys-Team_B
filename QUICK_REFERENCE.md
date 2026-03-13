# BudgetWise AI - Quick Reference Card

## 🚀 Quick Start

```bash
# Start Server
python manage.py runserver

# Access Application
http://127.0.0.1:8000/
```

---

## 🔗 Important URLs

| Page | URL |
|------|-----|
| **Login** | http://127.0.0.1:8000/accounts/login/ |
| **Signup** | http://127.0.0.1:8000/accounts/signup/ |
| **Dashboard** | http://127.0.0.1:8000/dashboard/ |
| **Add Expense** | http://127.0.0.1:8000/add-expense/ |
| **All Expenses** | http://127.0.0.1:8000/expenses/ |
| **Analytics** | http://127.0.0.1:8000/analytics/ |
| **AI Insights** | http://127.0.0.1:8000/ai/ai-insights/ |
| **Admin** | http://127.0.0.1:8000/admin/ |

---

## 📊 Features at a Glance

### Phase 1: Authentication ✅
- Register, Login, Logout
- Password Reset
- Secure Sessions

### Phase 2: Expenses ✅
- Add/Edit/Delete Expenses
- Set Monthly Budget
- 12 Categories

### Phase 3: Analytics ✅
- Dashboard with Charts
- Category Distribution
- Monthly Trends
- Filtering & Search

### Phase 4: AI ✅
- Expense Predictions
- Overspending Alerts
- Financial Insights
- Savings Advice

---

## 🎯 Common Tasks

### Add Expense
1. Click "Add Expense" in sidebar
2. Fill: Date, Amount, Category, Description
3. Click "Add Expense"

### Set Budget
1. Go to Dashboard
2. Find "Set Monthly Budget"
3. Select month, enter amount
4. Click "Save Budget"

### View AI Prediction
1. Add 3+ months of expenses
2. Click "🤖 AI Insights"
3. View prediction and insights

### Filter Expenses
1. Go to "All Expenses"
2. Select filters (Category/Month/Search)
3. Click "Apply Filters"

---

## 🔐 Default Credentials

### Test User
- **Username:** testuser
- **Password:** SecurePass123!

### Admin (if created)
- **Username:** admin
- **Password:** (your password)

---

## 📱 Sidebar Navigation

```
📊 Dashboard       - Main overview
➕ Add Expense     - Quick add
📋 All Expenses    - Full list
📈 Analytics       - Detailed stats
🤖 AI Insights     - ML predictions
```

---

## 🎨 Expense Categories

1. 🍔 Food
2. 🚗 Transport
3. 🏠 Rent
4. 🛍️ Shopping
5. 🎬 Entertainment
6. 💡 Bills
7. 🏥 Healthcare
8. 📚 Education
9. ✈️ Travel
10. 🛒 Groceries
11. ⚡ Utilities
12. 📦 Other

---

## 🤖 AI Requirements

**Minimum Data:** 3 months of expenses  
**Optimal Data:** 6-12 months  
**Confidence:** 60-95% (more data = higher)

---

## 📊 Charts Available

| Chart | Type | Location |
|-------|------|----------|
| Category Distribution | Doughnut | Dashboard |
| Monthly Expenses | Bar | Dashboard |
| Spending Trend | Line | Analytics |
| Expense Forecast | Line | AI Insights |

---

## 🔧 Troubleshooting

### Server Won't Start
```bash
python manage.py migrate
python manage.py runserver
```

### Charts Not Loading
- Refresh page
- Check internet (Chart.js CDN)
- Clear browser cache

### AI Shows "Insufficient Data"
- Add expenses for 3+ different months
- Ensure dates are correct
- Check user is logged in

### Budget Not Updating
- Verify month is selected
- Check amount is positive
- Refresh page

---

## 📝 Quick Commands

```bash
# Migrations
python manage.py makemigrations
python manage.py migrate

# Create Superuser
python manage.py createsuperuser

# Run Server
python manage.py runserver

# Run on Different Port
python manage.py runserver 8001

# Shell
python manage.py shell

# Check for Issues
python manage.py check
```

---

## 🗄️ Database

**Name:** budgetwise_db  
**Type:** PostgreSQL  
**Models:** User, Budget, Expense

---

## 📦 Dependencies

```
Django 5.0
PostgreSQL
scikit-learn
pandas
numpy
Chart.js
```

---

## 🎯 Key Metrics

| Metric | Value |
|--------|-------|
| Total Files | 60+ |
| Lines of Code | 7000+ |
| Pages | 10+ |
| API Endpoints | 13+ |
| Charts | 4 types |
| Categories | 12 |

---

## 🔐 Security

- ✅ CSRF Protection
- ✅ Password Hashing
- ✅ SQL Injection Protection
- ✅ XSS Protection
- ✅ Session Security

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| README.md | Overview |
| SETUP_GUIDE.md | Installation |
| QUICK_START_AI.md | AI Features |
| COMPLETE_TESTING_GUIDE.md | Testing |
| PROJECT_SUMMARY.md | Complete Summary |

---

## 🎉 Quick Tips

💡 **Tip 1:** Add expenses daily for best AI predictions  
💡 **Tip 2:** Use descriptions for better tracking  
💡 **Tip 3:** Review AI insights monthly  
💡 **Tip 4:** Set realistic budgets  
💡 **Tip 5:** Check analytics for patterns

---

## 🚨 Emergency Contacts

**GitHub Issues:** https://github.com/LalithaSriHarshitha/BudgetWiseAI/issues

---

## ✅ Status Check

```python
# Quick Status Check
✅ Server Running: http://127.0.0.1:8000/
✅ Database Connected: PostgreSQL
✅ Authentication: Working
✅ Expenses: Working
✅ Analytics: Working
✅ AI: Working
```

---

**Keep this card handy for quick reference!** 📌

**BudgetWise AI - Smart Finance Management** 💰🤖
