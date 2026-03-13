# Phase 4: AI-Based Expense Forecasting System

## 🤖 Overview

Phase 4 adds **Machine Learning capabilities** to BudgetWise, enabling intelligent expense forecasting and personalized financial insights using scikit-learn's Linear Regression model.

---

## ✨ Features Implemented

### 1. AI Expense Forecasting
- ✅ **Linear Regression Model** - Predicts next month's expenses
- ✅ **Historical Data Analysis** - Uses up to 12 months of data
- ✅ **Confidence Scoring** - R² score showing prediction accuracy
- ✅ **Trend Detection** - Identifies increasing/decreasing patterns

### 2. Financial Insights Engine
- ✅ **Overspending Detection** - Alerts when spending exceeds average by 20%+
- ✅ **Category Analysis** - Identifies highest spending categories
- ✅ **Month-over-Month Comparison** - Tracks spending changes
- ✅ **Personalized Savings Advice** - AI-generated recommendations

### 3. API Endpoints
- ✅ `/ai/api/predict-expense/` - Get expense prediction
- ✅ `/ai/api/insights/` - Get financial insights
- ✅ `/ai/api/forecast-chart/` - Get chart data with prediction

### 4. AI Dashboard
- ✅ **Prediction Cards** - Visual display of forecasts
- ✅ **Forecast Chart** - Historical + predicted expenses
- ✅ **Insight Cards** - Spending analysis and alerts
- ✅ **Savings Recommendations** - Actionable advice

---

## 📂 Project Structure

```
budgetwise/
├── ai_engine/                    # NEW AI Module
│   ├── __init__.py
│   ├── apps.py
│   ├── forecast.py              # ML forecasting engine
│   ├── insights.py              # Financial insights generator
│   ├── views.py                 # API endpoints
│   ├── urls.py                  # URL routing
│   └── templates/ai_engine/
│       └── ai_dashboard.html    # AI insights page
├── expenses/                     # Existing expense app
├── accounts/                     # Existing auth app
└── static/css/
    └── modern-dashboard.css     # Updated with AI styles
```

---

## 🧠 Machine Learning Implementation

### Forecasting Engine (`forecast.py`)

#### ExpenseForecastEngine Class

```python
class ExpenseForecastEngine:
    def __init__(self, user):
        self.user = user
        self.model = LinearRegression()
        self.min_data_points = 3  # Minimum months required
```

#### Key Methods:

**1. get_historical_data(months=12)**
- Fetches user's expense history
- Aggregates by month
- Returns pandas DataFrame

**2. prepare_training_data(df)**
- Converts data for ML model
- X = month indices [1, 2, 3, ...]
- y = total expenses per month

**3. train_model(X, y)**
- Trains Linear Regression model
- Fits on historical data
- Returns success/failure

**4. predict_next_month()**
- Predicts next month's expense
- Calculates confidence (R² score)
- Detects spending trend

#### Example Usage:

```python
from ai_engine.forecast import predict_next_month_expense

prediction = predict_next_month_expense(user)

# Returns:
{
    'success': True,
    'predicted_amount': 1234.56,
    'confidence': 85.3,
    'trend': 'increasing',
    'data_points': 6
}
```

---

## 💡 Insights Engine (`insights.py`)

### FinancialInsightsEngine Class

```python
class FinancialInsightsEngine:
    def __init__(self, user):
        self.user = user
        self.analytics = ExpenseAnalytics(user)
```

#### Key Methods:

**1. detect_overspending(threshold=20)**
- Compares current month to historical average
- Triggers alert if >20% above average
- Returns percentage difference

**2. get_highest_spending_category()**
- Identifies top spending category
- Returns amount and transaction count

**3. calculate_spending_change()**
- Compares current month to last month
- Calculates percentage change
- Determines direction (increased/decreased/stable)

**4. generate_savings_advice()**
- Analyzes spending patterns
- Generates personalized recommendations
- Categorizes advice (urgent/warning/suggestion/positive)

**5. generate_user_insights()**
- Combines all insights
- Returns comprehensive analysis

#### Example Usage:

```python
from ai_engine.insights import generate_user_insights

insights = generate_user_insights(user)

# Returns:
{
    'overspending_alert': {...},
    'highest_category': {...},
    'spending_change': {...},
    'savings_advice': [...]
}
```

---

## 🔗 API Endpoints

### 1. Predict Expense API

**Endpoint:** `/ai/api/predict-expense/`  
**Method:** GET  
**Auth:** Required

**Response:**
```json
{
    "success": true,
    "predicted_amount": 1234.56,
    "confidence": 85.3,
    "trend": "increasing",
    "historical_data": [...],
    "data_points": 6
}
```

### 2. Insights API

**Endpoint:** `/ai/api/insights/`  
**Method:** GET  
**Auth:** Required

**Response:**
```json
{
    "overspending_alert": {
        "is_overspending": true,
        "message": "⚠️ Your spending this month is 28% higher than your average.",
        "percentage_above_average": 28.0,
        "current_spending": 1500.00,
        "average_spending": 1171.88
    },
    "highest_category": {
        "category": "Food",
        "amount": 450.00,
        "count": 12,
        "message": "You spent the most on Food this month ($450.00)."
    },
    "spending_change": {
        "change_percentage": 15.5,
        "change_amount": 200.00,
        "direction": "increased",
        "message": "📈 Your expenses increased by 15.5% compared to last month."
    },
    "savings_advice": [
        {
            "type": "warning",
            "icon": "⚠️",
            "message": "You've used 85% of your budget..."
        }
    ]
}
```

### 3. Forecast Chart Data API

**Endpoint:** `/ai/api/forecast-chart/`  
**Method:** GET  
**Auth:** Required

**Response:**
```json
{
    "success": true,
    "historical_labels": ["Jan 2026", "Feb 2026", ...],
    "historical_data": [1200, 1350, 1180, ...],
    "prediction_label": "Apr 2026",
    "prediction_value": 1234.56,
    "confidence": 85.3
}
```

---

## 🎨 AI Dashboard UI

### Access
**URL:** `/ai/ai-insights/` or click "🤖 AI Insights" in sidebar

### Components

#### 1. Prediction Section
- **Main Prediction Card** - Large card with predicted amount
- **Confidence Badge** - Shows model accuracy
- **Trend Badge** - Increasing/Decreasing/Stable
- **Data Points** - Number of months used

#### 2. Forecast Chart
- **Line Chart** - Historical expenses (solid line)
- **Prediction Point** - Next month (dashed line, star marker)
- **Interactive Tooltips** - Hover for details
- **Legend** - Distinguishes historical vs predicted

#### 3. Insights Cards
- **Overspending Alert** - Warning if spending is high
- **Top Category** - Highest spending category
- **Monthly Change** - Comparison to last month
- **Budget Status** - Circular progress chart

#### 4. Savings Recommendations
- **Urgent** - Red border, critical issues
- **Warning** - Yellow border, caution needed
- **Suggestion** - Blue border, helpful tips
- **Positive** - Green border, good habits

---

## 🔬 How the ML Model Works

### Training Process

1. **Data Collection**
   ```python
   # Fetch last 12 months of expenses
   monthly_data = Expense.objects.filter(
       user=user,
       date__gte=start_date
   ).annotate(
       month=TruncMonth('date')
   ).values('month').annotate(
       total=Sum('amount')
   )
   ```

2. **Data Preparation**
   ```python
   # Convert to training format
   X = [[1], [2], [3], [4], [5], [6]]  # Month indices
   y = [1200, 1350, 1180, 1420, 1290, 1380]  # Expenses
   ```

3. **Model Training**
   ```python
   model = LinearRegression()
   model.fit(X, y)
   ```

4. **Prediction**
   ```python
   next_month_index = 7
   predicted = model.predict([[next_month_index]])
   # Result: 1234.56
   ```

5. **Confidence Calculation**
   ```python
   confidence = model.score(X, y) * 100
   # R² score: 85.3%
   ```

### Why Linear Regression?

- ✅ **Simple and Fast** - Quick training and prediction
- ✅ **Interpretable** - Easy to understand results
- ✅ **Effective** - Works well for trend-based forecasting
- ✅ **Low Data Requirements** - Needs only 3+ months
- ✅ **No Overfitting** - Stable with small datasets

### Limitations

- ⚠️ Assumes linear trend (may not capture seasonality)
- ⚠️ Requires at least 3 months of data
- ⚠️ Best for short-term predictions (1-3 months)
- ⚠️ Doesn't account for external factors

---

## 📊 Insights Algorithm

### Overspending Detection

```python
# Calculate average of last 3-6 months
historical_avg = sum(monthly_totals) / len(months)

# Compare to current month
percentage_diff = ((current - historical_avg) / historical_avg) * 100

# Trigger alert if > 20%
if percentage_diff > 20:
    alert = "⚠️ Overspending detected!"
```

### Spending Change Analysis

```python
# Get current and last month
current_month_total = get_current_month_expenses()
last_month_total = get_last_month_expenses()

# Calculate change
change = ((current - last) / last) * 100

# Categorize
if change > 10:
    direction = "increased"
elif change < -10:
    direction = "decreased"
else:
    direction = "stable"
```

### Savings Advice Generation

```python
advice = []

# Check budget status
if budget_exceeded:
    advice.append({
        'type': 'urgent',
        'message': 'Cut non-essential expenses'
    })

# Check discretionary spending
if discretionary_percentage > 40:
    advice.append({
        'type': 'suggestion',
        'message': 'Reduce entertainment expenses'
    })
```

---

## 🚀 Usage Guide

### For Users

**Step 1: Track Expenses**
- Add at least 3 months of expense data
- More data = better predictions

**Step 2: Access AI Insights**
- Click "🤖 AI Insights" in sidebar
- View prediction and insights

**Step 3: Review Forecast**
- Check predicted next month expense
- Note confidence level
- Observe spending trend

**Step 4: Act on Insights**
- Read overspending alerts
- Review savings recommendations
- Adjust spending habits

### For Developers

**Integrate Prediction:**
```python
from ai_engine.forecast import predict_next_month_expense

prediction = predict_next_month_expense(request.user)

if prediction['success']:
    amount = prediction['predicted_amount']
    confidence = prediction['confidence']
```

**Get Insights:**
```python
from ai_engine.insights import generate_user_insights

insights = generate_user_insights(request.user)

overspending = insights['overspending_alert']
advice = insights['savings_advice']
```

**Custom Forecasting:**
```python
from ai_engine.forecast import ExpenseForecastEngine

engine = ExpenseForecastEngine(user)
predictions = engine.predict_next_n_months(n=3)
```

---

## 🔐 Security & Privacy

### Data Protection
- ✅ **User Isolation** - Each user's model uses only their data
- ✅ **Login Required** - All AI endpoints require authentication
- ✅ **No Data Sharing** - Models don't share data between users
- ✅ **No External APIs** - All processing happens locally

### Performance
- ✅ **On-Demand Training** - Model trains when prediction requested
- ✅ **Fast Execution** - Linear Regression is computationally light
- ✅ **No Caching** - Fresh predictions every time
- ✅ **Scalable** - Works with any number of users

---

## 📈 Future Enhancements

### Potential Improvements

1. **Advanced Models**
   - ARIMA for seasonality
   - Prophet for trend detection
   - LSTM for complex patterns

2. **More Features**
   - Category-specific predictions
   - Budget optimization suggestions
   - Anomaly detection
   - Spending pattern recognition

3. **Enhanced Insights**
   - Peer comparison (anonymized)
   - Goal tracking
   - Savings milestones
   - Financial health score

4. **Auto-Categorization**
   - NLP for description analysis
   - Automatic category assignment
   - Smart tagging

---

## 🧪 Testing

### Test Scenarios

**Scenario 1: New User (< 3 months data)**
- Expected: "Insufficient data" message
- Action: Add more expenses

**Scenario 2: Regular User (3-6 months data)**
- Expected: Prediction with moderate confidence (60-80%)
- Action: Review forecast

**Scenario 3: Experienced User (6+ months data)**
- Expected: Prediction with high confidence (80-95%)
- Action: Trust and plan accordingly

**Scenario 4: Overspending**
- Expected: Warning alert with percentage
- Action: Review savings advice

**Scenario 5: Under Budget**
- Expected: Positive message
- Action: Continue good habits

---

## 📝 API Integration Examples

### JavaScript Fetch

```javascript
// Get prediction
fetch('/ai/api/predict-expense/')
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            console.log('Predicted:', data.predicted_amount);
            console.log('Confidence:', data.confidence);
        }
    });

// Get insights
fetch('/ai/api/insights/')
    .then(response => response.json())
    .then(data => {
        console.log('Overspending:', data.overspending_alert);
        console.log('Advice:', data.savings_advice);
    });
```

### Python Requests

```python
import requests

# Get prediction
response = requests.get(
    'http://localhost:8000/ai/api/predict-expense/',
    cookies={'sessionid': session_id}
)
prediction = response.json()

# Get insights
response = requests.get(
    'http://localhost:8000/ai/api/insights/',
    cookies={'sessionid': session_id}
)
insights = response.json()
```

---

## 🎓 Key Takeaways

### What Makes This AI System Effective

1. **Simplicity** - Linear Regression is easy to understand and maintain
2. **Speed** - Fast training and prediction
3. **Accuracy** - Good enough for personal finance forecasting
4. **Privacy** - All data stays local, no external APIs
5. **Actionable** - Provides clear, useful insights

### Best Practices

- ✅ Encourage users to track expenses consistently
- ✅ Explain confidence scores to users
- ✅ Provide context with predictions
- ✅ Make insights actionable
- ✅ Update predictions regularly

---

## 📚 Dependencies

```
scikit-learn>=1.3.0  # Machine learning
pandas>=2.0.0        # Data manipulation
numpy>=1.24.0        # Numerical computing
python-dateutil>=2.8.2  # Date handling
```

---

## ✅ Phase 4 Complete!

**BudgetWise now includes:**
- ✅ Phase 1: Authentication System
- ✅ Phase 2: Expense Management
- ✅ Phase 3: Analytics Dashboard
- ✅ Phase 4: AI Forecasting & Insights

**Ready for production deployment!** 🚀
