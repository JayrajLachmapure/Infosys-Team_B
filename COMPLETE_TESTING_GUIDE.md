# Complete Testing Guide - BudgetWise AI

## 🎯 All Features Testing Checklist

This guide covers testing all 4 phases of BudgetWise.

---

## 📋 Pre-Testing Setup

### 1. Verify Server is Running
```bash
python manage.py runserver
```
**Expected:** Server running at http://127.0.0.1:8000/

### 2. Verify Database Connection
- PostgreSQL should be running
- Database `budgetwise_db` should exist
- Migrations should be applied

### 3. Create Test User
**Option A:** Use existing account  
**Option B:** Create new test account

---

## Phase 1: Authentication System ✅

### Test 1.1: User Registration

**Steps:**
1. Go to http://127.0.0.1:8000/accounts/signup/
2. Fill in form:
   - Username: `testuser`
   - Email: `test@example.com`
   - Password: `SecurePass123!`
   - Confirm Password: `SecurePass123!`
3. Click "Create Account"

**Expected Results:**
- ✅ Success message appears
- ✅ Redirected to login page
- ✅ User saved in database

**Test Invalid Data:**
- Weak password → Error message
- Duplicate username → Error message
- Invalid email → Error message
- Passwords don't match → Error message

### Test 1.2: User Login

**Steps:**
1. Go to http://127.0.0.1:8000/accounts/login/
2. Enter credentials
3. Click "Sign In"

**Expected Results:**
- ✅ Welcome message appears
- ✅ Redirected to dashboard
- ✅ User info displayed

**Test Invalid Login:**
- Wrong password → Error message
- Non-existent user → Error message

### Test 1.3: Password Visibility Toggle

**Steps:**
1. On login/signup page
2. Click eye icon next to password field

**Expected Results:**
- ✅ Password becomes visible
- ✅ Icon changes
- ✅ Click again to hide

### Test 1.4: Password Reset

**Steps:**
1. Click "Forgot password?" on login page
2. Enter email address
3. Check console/terminal for reset link
4. Copy link and open in browser
5. Set new password

**Expected Results:**
- ✅ Email sent confirmation
- ✅ Reset link in console
- ✅ Password reset successful
- ✅ Can login with new password

### Test 1.5: Logout

**Steps:**
1. Click "Logout" button
2. Try accessing dashboard

**Expected Results:**
- ✅ Redirected to login
- ✅ Cannot access protected pages
- ✅ Session cleared

---

## Phase 2: Expense Management ✅

### Test 2.1: Set Monthly Budget

**Steps:**
1. Login and go to dashboard
2. Find "Set Monthly Budget" section
3. Select current month
4. Enter amount: `2000`
5. Click "Save Budget"

**Expected Results:**
- ✅ Success message
- ✅ Budget displayed
- ✅ Remaining budget shown
- ✅ Progress bar appears

### Test 2.2: Add Expense

**Steps:**
1. Click "Add Expense" in sidebar
2. Fill form:
   - Date: Today
   - Amount: `50.00`
   - Category: Food
   - Description: "Lunch at restaurant"
3. Click "Add Expense"

**Expected Results:**
- ✅ Success message
- ✅ Redirected to dashboard
- ✅ Expense appears in list
- ✅ Budget calculations update

**Add Multiple Expenses:**
- Rent: $1200
- Groceries: $300
- Transport: $100
- Entertainment: $80

### Test 2.3: View All Expenses

**Steps:**
1. Click "All Expenses" in sidebar
2. View expense table

**Expected Results:**
- ✅ All expenses listed
- ✅ Pagination works (if >15 expenses)
- ✅ Total amount shown
- ✅ Transaction count displayed

### Test 2.4: Filter Expenses

**Steps:**
1. On "All Expenses" page
2. Select category filter: "Food"
3. Click "Apply Filters"

**Expected Results:**
- ✅ Only Food expenses shown
- ✅ Total recalculated
- ✅ Count updated

**Test Other Filters:**
- Month filter
- Search by description
- Combine multiple filters

### Test 2.5: Edit Expense

**Steps:**
1. On "All Expenses" page
2. Click edit icon (✏️) on any expense
3. Change amount to `75.00`
4. Click "Update Expense"

**Expected Results:**
- ✅ Success message
- ✅ Expense updated in list
- ✅ Calculations updated

### Test 2.6: Delete Expense

**Steps:**
1. Click delete icon (🗑️) on any expense
2. Confirm deletion

**Expected Results:**
- ✅ Confirmation dialog
- ✅ Expense removed
- ✅ Success message
- ✅ Calculations updated

---

## Phase 3: Analytics Dashboard ✅

### Test 3.1: Dashboard Summary Cards

**Steps:**
1. Go to main dashboard
2. View summary cards

**Expected Results:**
- ✅ Total Expenses card shows correct amount
- ✅ Transactions card shows count
- ✅ Top Category card shows highest
- ✅ Budget Status card shows remaining

### Test 3.2: Category Distribution Chart

**Steps:**
1. View doughnut chart on dashboard
2. Hover over segments

**Expected Results:**
- ✅ Chart displays categories
- ✅ Colors are distinct
- ✅ Tooltips show amounts
- ✅ Legend displays correctly

### Test 3.3: Monthly Expenses Chart

**Steps:**
1. View bar chart on dashboard
2. Check last 6 months

**Expected Results:**
- ✅ Bars show monthly totals
- ✅ Labels show month names
- ✅ Tooltips show amounts
- ✅ Y-axis shows dollar amounts

### Test 3.4: Analytics Page

**Steps:**
1. Click "Analytics" in sidebar
2. View detailed analytics

**Expected Results:**
- ✅ Summary cards display
- ✅ 30-day trend chart shows
- ✅ Category breakdown table
- ✅ Percentage bars display

### Test 3.5: Responsive Design

**Steps:**
1. Resize browser window
2. Test on mobile size

**Expected Results:**
- ✅ Layout adapts
- ✅ Sidebar behavior changes
- ✅ Cards stack vertically
- ✅ Charts remain readable

---

## Phase 4: AI Forecasting ✅

### Test 4.1: Insufficient Data Scenario

**Steps:**
1. Create new user with <3 months data
2. Go to AI Insights page

**Expected Results:**
- ✅ "Insufficient data" message
- ✅ Explanation shown
- ✅ Minimum requirement stated

### Test 4.2: AI Expense Prediction

**Prerequisites:** 3+ months of expense data

**Steps:**
1. Click "🤖 AI Insights" in sidebar
2. View prediction card

**Expected Results:**
- ✅ Predicted amount displayed
- ✅ Confidence percentage shown
- ✅ Trend indicator (increasing/decreasing/stable)
- ✅ Data points count shown

**Verify Prediction:**
- Should be reasonable based on history
- Confidence should be 60-95%
- Trend should match pattern

### Test 4.3: Forecast Chart

**Steps:**
1. On AI Insights page
2. View forecast chart

**Expected Results:**
- ✅ Historical data (blue solid line)
- ✅ Prediction point (green dashed line, star)
- ✅ Month labels on X-axis
- ✅ Dollar amounts on Y-axis
- ✅ Legend shows both datasets
- ✅ Tooltips work on hover

### Test 4.4: Overspending Detection

**Test Case A: Normal Spending**
- Current month: $1200
- Average: $1150
- Expected: "Within normal range" ✅

**Test Case B: Overspending**
- Current month: $1500
- Average: $1100
- Expected: "28% higher than average" ⚠️

**Test Case C: Under Budget**
- Current month: $900
- Average: $1200
- Expected: "25% lower than average" ✅

**Steps:**
1. View overspending alert card
2. Check message and percentage

**Expected Results:**
- ✅ Correct alert type (success/warning)
- ✅ Accurate percentage
- ✅ Current vs average shown
- ✅ Appropriate icon

### Test 4.5: Highest Category Insight

**Steps:**
1. View "Top Category" card
2. Check category and amount

**Expected Results:**
- ✅ Shows category with most spending
- ✅ Displays total amount
- ✅ Shows transaction count
- ✅ Message is clear

### Test 4.6: Spending Change Analysis

**Steps:**
1. View "Monthly Change" card
2. Check percentage and direction

**Expected Results:**
- ✅ Compares to last month
- ✅ Shows percentage change
- ✅ Indicates direction (↑↓→)
- ✅ Color coding (red/green)

### Test 4.7: Budget Status Circle

**Steps:**
1. View "Budget Status" card
2. Check circular progress

**Expected Results:**
- ✅ Circle shows percentage used
- ✅ Percentage number in center
- ✅ Remaining amount shown
- ✅ Animation on load

### Test 4.8: Savings Recommendations

**Steps:**
1. Scroll to "Savings Recommendations"
2. View advice cards

**Expected Results:**
- ✅ Multiple recommendations shown
- ✅ Categorized by type (urgent/warning/suggestion/positive)
- ✅ Color-coded borders
- ✅ Actionable advice
- ✅ Relevant to user's situation

**Advice Types:**
- 🚨 Urgent (red) - Budget exceeded
- ⚠️ Warning (yellow) - High usage
- 💡 Suggestion (blue) - Optimization tips
- ✅ Positive (green) - Good habits

### Test 4.9: API Endpoints

**Test Predict API:**
```bash
# In browser or Postman (must be logged in)
GET http://127.0.0.1:8000/ai/api/predict-expense/
```

**Expected Response:**
```json
{
    "success": true,
    "predicted_amount": 1234.56,
    "confidence": 85.3,
    "trend": "increasing",
    "data_points": 6
}
```

**Test Insights API:**
```bash
GET http://127.0.0.1:8000/ai/api/insights/
```

**Expected Response:**
```json
{
    "overspending_alert": {...},
    "highest_category": {...},
    "spending_change": {...},
    "savings_advice": [...]
}
```

**Test Forecast Chart API:**
```bash
GET http://127.0.0.1:8000/ai/api/forecast-chart/
```

**Expected Response:**
```json
{
    "success": true,
    "historical_labels": ["Jan 2026", ...],
    "historical_data": [1200, 1350, ...],
    "prediction_label": "Apr 2026",
    "prediction_value": 1234.56
}
```

---

## 🎯 Complete User Journey Test

### Scenario: New User Complete Flow

**Day 1: Setup**
1. Register account
2. Login
3. Set monthly budget: $2000

**Week 1: Add Expenses**
1. Add rent: $1200
2. Add groceries: $150
3. Add transport: $50
4. Add food: $80

**Week 2: More Expenses**
1. Add groceries: $120
2. Add entertainment: $60
3. Add utilities: $100

**Week 3: Review**
1. View dashboard
2. Check budget status
3. View analytics
4. Filter expenses by category

**Week 4: Month End**
1. Review total spending
2. Compare to budget
3. Note: Need 2 more months for AI

**Month 2-3: Continue Tracking**
1. Set new monthly budgets
2. Add expenses consistently
3. Track different categories

**Month 4: AI Insights**
1. Access AI Insights page
2. View prediction
3. Check overspending alerts
4. Review recommendations
5. Adjust spending based on insights

---

## 🐛 Common Issues & Solutions

### Issue: Charts Not Loading
**Solution:** 
- Check browser console for errors
- Verify Chart.js CDN is accessible
- Refresh page

### Issue: Prediction Shows "Insufficient Data"
**Solution:**
- Add expenses for at least 3 different months
- Ensure expenses are in different months
- Check date fields are correct

### Issue: Budget Not Updating
**Solution:**
- Verify month is selected
- Check amount is positive
- Refresh page

### Issue: Expenses Not Appearing
**Solution:**
- Check date is in current month
- Verify user is logged in
- Check filters are not applied

### Issue: AI Insights Not Accurate
**Solution:**
- Add more historical data
- Ensure consistent tracking
- Check for data entry errors

---

## ✅ Final Verification Checklist

### Authentication
- [ ] Can register new user
- [ ] Can login
- [ ] Can logout
- [ ] Password reset works
- [ ] Password visibility toggle works

### Expense Management
- [ ] Can set budget
- [ ] Can add expense
- [ ] Can edit expense
- [ ] Can delete expense
- [ ] Can view all expenses
- [ ] Filters work
- [ ] Search works
- [ ] Pagination works

### Analytics
- [ ] Dashboard loads
- [ ] Summary cards show correct data
- [ ] Category chart displays
- [ ] Monthly chart displays
- [ ] Analytics page works
- [ ] Trend chart shows

### AI Features
- [ ] AI Insights page loads
- [ ] Prediction displays (with 3+ months data)
- [ ] Forecast chart shows
- [ ] Overspending detection works
- [ ] Highest category identified
- [ ] Spending change calculated
- [ ] Budget status shows
- [ ] Savings advice generated
- [ ] API endpoints return data

### UI/UX
- [ ] Sidebar navigation works
- [ ] All links functional
- [ ] Responsive on mobile
- [ ] Charts are interactive
- [ ] Messages auto-hide
- [ ] Forms validate
- [ ] Buttons have hover effects
- [ ] Colors are consistent

### Security
- [ ] Login required for protected pages
- [ ] Users see only their data
- [ ] CSRF tokens present
- [ ] Passwords are hashed
- [ ] SQL injection protected

---

## 📊 Performance Benchmarks

### Expected Load Times
- Dashboard: < 2 seconds
- AI Insights: < 3 seconds
- Expense List: < 2 seconds
- Charts: < 1 second to render

### Database Queries
- Dashboard: ~5-8 queries
- AI Prediction: ~3-5 queries
- Expense List: ~2-3 queries

---

## 🎉 Testing Complete!

If all tests pass:
- ✅ All 4 phases working
- ✅ Authentication secure
- ✅ Expense management functional
- ✅ Analytics accurate
- ✅ AI predictions working
- ✅ UI responsive
- ✅ Security implemented

**BudgetWise is production-ready!** 🚀

---

## 📝 Test Report Template

```
Test Date: ___________
Tester: ___________
Environment: Development/Production

Phase 1 (Authentication): PASS / FAIL
Phase 2 (Expenses): PASS / FAIL
Phase 3 (Analytics): PASS / FAIL
Phase 4 (AI): PASS / FAIL

Issues Found:
1. ___________
2. ___________

Notes:
___________
```

---

**Happy Testing!** 🧪✨
