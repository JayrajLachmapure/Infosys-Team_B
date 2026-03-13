<<<<<<< HEAD
# BudgetWise - AI-Based Expense Forecasting Tool

**Complete Personal Finance Management with Machine Learning**

Production-grade Django application with AI-powered expense forecasting, comprehensive analytics, and modern UI.

---

## 🚀 Features

### Phase 1: Authentication System ✅
- User registration with validation
- Secure login/logout
- Password reset via email
- Password visibility toggle
- Strong password enforcement
- PostgreSQL database

### Phase 2: Expense Management ✅
- Complete CRUD operations
- 12 expense categories
- Budget tracking
- Monthly budget setting
- Real-time calculations

### Phase 3: Analytics Dashboard ✅
- Modern card-based UI
- Chart.js visualizations
- Category distribution
- Monthly trends
- Spending analysis
- Responsive design

### Phase 4: AI Forecasting ✅ NEW!
- **Machine Learning predictions**
- **Linear Regression model**
- **Overspending detection**
- **Financial insights**
- **Savings recommendations**
- **Forecast charts**

---

## 🤖 AI Features

### Expense Forecasting
- Predicts next month's expenses
- Uses historical data (3-12 months)
- Confidence scoring (R² score)
- Trend detection (increasing/decreasing/stable)

### Financial Insights
- Overspending alerts (20%+ threshold)
- Highest spending category analysis
- Month-over-month comparison
- Budget status tracking

### Savings Recommendations
- Personalized advice
- Urgency categorization
- Actionable suggestions
- Pattern-based insights

---

## 📊 Tech Stack

**Backend:**
- Django 5.0
- PostgreSQL
- Python 3.10+

**Machine Learning:**
- scikit-learn (Linear Regression)
- pandas (Data processing)
- numpy (Numerical computing)

**Frontend:**
- HTML5/CSS3
- Vanilla JavaScript
- Chart.js (Visualizations)

**Authentication:**
- Django built-in auth
- Session-based
- CSRF protection

---

## 🎯 Quick Start

### Prerequisites
- Python 3.10+
- PostgreSQL 14+
- pip

### Installation

```bash
# 1. Clone repository
git clone https://github.com/LalithaSriHarshitha/BudgetWiseAI.git
cd BudgetWiseAI

# 2. Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Create PostgreSQL database
# In PostgreSQL: CREATE DATABASE budgetwise_db;

# 5. Configure environment
# Copy .env.example to .env and update credentials

# 6. Run migrations
python manage.py migrate

# 7. Create superuser (optional)
python manage.py createsuperuser

# 8. Start server
python manage.py runserver
```

### Access Application
- **Main URL:** http://127.0.0.1:8000/
- **Dashboard:** http://127.0.0.1:8000/dashboard/
- **AI Insights:** http://127.0.0.1:8000/ai/ai-insights/
- **Admin:** http://127.0.0.1:8000/admin/

---

## 📱 Screenshots

### Dashboard
Modern card-based layout with summary metrics and charts

### AI Insights
Machine learning predictions with confidence scores

### Expense Management
Complete CRUD with filtering and search

### Analytics
Detailed spending analysis with visualizations

---

## 🗄️ Database Models

### User (Django built-in)
- username, email, password
- Authentication fields

### Budget
- user, month, amount
- Monthly budget tracking

### Expense
- user, amount, category, description, date
- Expense entries with categorization

---

## 🔗 API Endpoints

### Expense Management
- `GET /dashboard/` - Main dashboard
- `GET /add-expense/` - Add expense form
- `GET /expenses/` - List all expenses
- `GET /analytics/` - Analytics page

### AI Endpoints
- `GET /ai/api/predict-expense/` - Get prediction (JSON)
- `GET /ai/api/insights/` - Get insights (JSON)
- `GET /ai/api/forecast-chart/` - Get chart data (JSON)
- `GET /ai/ai-insights/` - AI dashboard page

---

## 🎨 UI Components

### Sidebar Navigation
- Dashboard
- Add Expense
- All Expenses
- Analytics
- AI Insights (NEW!)
- User Profile
- Logout

### Cards
- Summary cards with icons
- Prediction cards
- Insight cards
- Chart cards

### Charts
- Doughnut (category distribution)
- Bar (monthly trends)
- Line (spending trend)
- Forecast (historical + prediction)

---

## 🧠 Machine Learning

### Algorithm
**Linear Regression** - Simple, fast, interpretable

### Training Data
- Historical monthly expenses
- Minimum 3 months required
- Optimal: 6-12 months

### Prediction Process
1. Fetch user's expense history
2. Aggregate by month
3. Prepare training data (X=months, y=amounts)
4. Train Linear Regression model
5. Predict next month
6. Calculate confidence (R² score)

### Example
```python
from ai_engine.forecast import predict_next_month_expense

prediction = predict_next_month_expense(user)
# Returns: {'predicted_amount': 1234.56, 'confidence': 85.3}
```

---

## 🔐 Security

- ✅ User authentication required
- ✅ Data isolation (users see only their data)
- ✅ CSRF protection on forms
- ✅ SQL injection protection (Django ORM)
- ✅ XSS protection (template escaping)
- ✅ Password hashing (PBKDF2)
- ✅ Session-based auth

---

## 📈 Performance

### Database
- Indexed queries (user + date, user + category)
- Efficient aggregations
- Optimized ORM queries

### ML Model
- Fast training (<1 second)
- On-demand predictions
- No caching needed
- Scalable to many users

### Frontend
- Minimal JavaScript
- CDN for Chart.js
- CSS animations (GPU accelerated)
- Responsive images

---

## 🧪 Testing

### Manual Testing
1. Register new user
2. Add 3+ months of expenses
3. Set monthly budget
4. View AI predictions
5. Check insights accuracy
6. Test CRUD operations

### Test Data
```python
# Add sample expenses
January: $1200 (Food: $400, Rent: $800)
February: $1350 (Food: $450, Rent: $800, Shopping: $100)
March: $1180 (Food: $380, Rent: $800)
```

---

## 📚 Documentation

- **PHASE4_AI_DOCUMENTATION.md** - Complete AI system docs
- **QUICK_START_AI.md** - Quick start guide
- **PHASE3_DOCUMENTATION.md** - Analytics system docs
- **SETUP_GUIDE.md** - Installation guide
- **README.md** - This file

---

## 🛠️ Development

### Project Structure
```
budgetwise/
├── accounts/          # Authentication
├── expenses/          # Expense management
├── ai_engine/         # AI forecasting (NEW!)
├── static/            # CSS, JS
├── templates/         # HTML templates
├── budgetwise/        # Django settings
└── manage.py
```

### Key Files
- `ai_engine/forecast.py` - ML forecasting engine
- `ai_engine/insights.py` - Financial insights
- `expenses/services.py` - Analytics logic
- `static/css/modern-dashboard.css` - UI styles

---

## 🚀 Deployment

### Production Checklist
- [ ] Set DEBUG=False
- [ ] Configure ALLOWED_HOSTS
- [ ] Use production database
- [ ] Set strong SECRET_KEY
- [ ] Configure email backend
- [ ] Set up static files serving
- [ ] Enable HTTPS
- [ ] Configure logging

### Environment Variables
```env
DB_NAME=budgetwise_db
DB_USER=postgres
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
SECRET_KEY=your_secret_key
DEBUG=False
```

---

## 🤝 Contributing

1. Fork the repository
2. Create feature branch
3. Commit changes
4. Push to branch
5. Create Pull Request

---

## 📝 License

MIT License - See LICENSE file

---

## 👥 Authors

- **Lalitha Sri Harshitha** - Initial work

---

## 🙏 Acknowledgments

- Django framework
- scikit-learn library
- Chart.js visualization
- PostgreSQL database

---

## 📞 Support

- **GitHub:** https://github.com/LalithaSriHarshitha/BudgetWiseAI
- **Issues:** https://github.com/LalithaSriHarshitha/BudgetWiseAI/issues

---

## 🎯 Roadmap

### Future Enhancements
- [ ] Advanced ML models (ARIMA, Prophet)
- [ ] Category-specific predictions
- [ ] Anomaly detection
- [ ] Mobile app
- [ ] Export to CSV/PDF
- [ ] Multi-currency support
- [ ] Recurring expenses
- [ ] Bill reminders

---

## ⭐ Star History

If you find this project useful, please consider giving it a star!

---

**Built with ❤️ using Django, PostgreSQL, and Machine Learning**
=======
# Infosys-Team_B
Team Project
>>>>>>> 5306a5cb64b7c68146fe439803e21bfc9dc4119b
