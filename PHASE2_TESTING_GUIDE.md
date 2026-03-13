# Phase 2 Testing Guide - Expense Management Dashboard

## 🎉 What's New in Phase 2

✅ Complete Expense Management Dashboard
✅ Set Monthly Budget
✅ Add Daily Expenses
✅ View Today's Expenses
✅ Budget Overview with Chart.js Visualization
✅ Dynamic Calculations (Spent + Remaining)
✅ User-specific Data (Each user sees only their data)
✅ CRUD Operations (Create, Read, Delete)

---

## 🚀 Quick Start

### Server is Running at:
**http://127.0.0.1:8000/**

After login, you'll be automatically redirected to the dashboard.

---

## 📋 Testing Checklist

### 1. User Authentication (Already Working)

✅ **Register a New User**
- Go to: http://127.0.0.1:8000/accounts/signup/
- Create account with:
  - Username: `testuser1`
  - Email: `test1@example.com`
  - Password: `SecurePass123!`

✅ **Login**
- Go to: http://127.0.0.1:8000/accounts/login/
- Login with your credentials
- **You should be redirected to the dashboard automatically**

---

### 2. Set Monthly Budget

**Location:** Left section, top card

**Steps:**
1. After login, you'll see "📊 Set Monthly Budget" card
2. Select month from dropdown (current month is default)
3. Enter budget amount (e.g., `2000`)
4. Click "Save Budget"

**Expected Results:**
- ✅ Success message: "Budget set successfully for [Month]!"
- ✅ Budget summary appears showing:
  - Current Budget: $2000.00
  - Remaining: $2000.00
- ✅ Chart updates to show full budget as "Remaining" (green)

**Test Cases:**
- ✅ Set budget for current month
- ✅ Update existing budget (change amount)
- ✅ Set budget for future months
- ✅ Try negative amount (should fail validation)

---

### 3. Add Daily Expenses

**Location:** Left section, middle card

**Steps:**
1. Fill in the "➕ Add Daily Expense" form:
   - Date: Today's date (auto-filled)
   - Amount: `50.00`
   - Category: Select "Groceries"
   - Note: "Weekly grocery shopping" (optional)
2. Click "Add Expense"

**Expected Results:**
- ✅ Success message: "Expense of $50.00 added successfully!"
- ✅ Expense appears in "Today's Expenses" section
- ✅ Expense appears in "All Expenses This Month" section
- ✅ Budget calculations update:
  - Total Spent: $50.00
  - Remaining: $1950.00
- ✅ Chart updates to show spent (red) and remaining (green)

**Test Multiple Expenses:**
Add these expenses to test different categories:

| Amount | Category | Note |
|--------|----------|------|
| $50 | Groceries | Weekly shopping |
| $1200 | Rent | Monthly rent |
| $30 | Food | Lunch with friends |
| $100 | Travel | Gas for car |
| $80 | Utilities | Electricity bill |

**Expected After All Expenses:**
- Total Spent: $1460.00
- Remaining: $540.00
- Chart shows proportional split

---

### 4. View Today's Expenses

**Location:** Left section, bottom card

**What to Check:**
- ✅ Only expenses added today appear here
- ✅ Each expense shows:
  - Category icon (emoji)
  - Category name
  - Note (truncated if long)
  - Amount
  - Delete button (🗑️)
- ✅ If no expenses today: "No expenses added today."

---

### 5. Budget Overview Card

**Location:** Right section, top card

**What to Check:**
- ✅ Shows current month name (e.g., "February 2026")
- ✅ Three stat boxes:
  - **Monthly Budget** (blue): $2000.00
  - **Total Spent** (red): $1460.00
  - **Remaining** (green): $540.00
- ✅ Donut chart displays:
  - Red section: Spent amount
  - Green section: Remaining amount
  - Hover shows exact values
- ✅ If budget exceeded: Warning message appears

**Test Budget Exceeded:**
1. Add expense of $600
2. Remaining becomes negative: -$60.00
3. Warning appears: "⚠️ You've exceeded your budget by $60.00"
4. Remaining value turns red

---

### 6. All Expenses This Month

**Location:** Right section, bottom card

**What to Check:**
- ✅ Shows all expenses for current month
- ✅ Each expense displays:
  - Category icon (🛒 🏠 ✈️ 🍔 💡 etc.)
  - Category name
  - Date (formatted: "Feb 09, 2026")
  - Note (if provided)
  - Amount
  - Delete button
- ✅ Scrollable if many expenses
- ✅ Sorted by date (newest first)

---

### 7. Delete Expense

**Steps:**
1. Find any expense in the list
2. Click the delete button (🗑️)
3. Confirm deletion in popup

**Expected Results:**
- ✅ Confirmation dialog appears
- ✅ After confirming:
  - Success message: "Expense of $[amount] deleted successfully!"
  - Expense removed from list
  - Budget calculations update automatically
  - Chart updates to reflect new totals

---

### 8. User Data Isolation

**Test Multi-User Scenario:**

1. **Create Second User:**
   - Logout from first account
   - Register new user: `testuser2`
   - Login as `testuser2`

2. **Verify Isolation:**
   - ✅ Dashboard is empty (no budget set)
   - ✅ No expenses from `testuser1` visible
   - ✅ Set different budget (e.g., $3000)
   - ✅ Add different expenses

3. **Switch Back:**
   - Logout from `testuser2`
   - Login as `testuser1`
   - ✅ Original budget and expenses still there
   - ✅ No data from `testuser2` visible

**This confirms each user sees only their own data!**

---

### 9. Responsive Design

**Test on Different Screen Sizes:**

**Desktop (1400px+):**
- ✅ Two-column layout
- ✅ Left section: Budget + Expense forms + Today's expenses
- ✅ Right section: Overview + All expenses

**Tablet (768px - 1024px):**
- ✅ Single column layout
- ✅ Cards stack vertically
- ✅ All features accessible

**Mobile (< 768px):**
- ✅ Header stacks vertically
- ✅ Stats display in single column
- ✅ Expense items wrap properly
- ✅ Forms remain usable

---

### 10. Chart Visualization

**Chart.js Donut Chart:**

**What to Test:**
- ✅ Chart loads on page load
- ✅ Shows two segments:
  - Red: Spent amount
  - Green: Remaining amount
- ✅ Hover over segments shows exact values
- ✅ Legend at bottom shows labels
- ✅ Chart updates when page refreshes after adding/deleting expenses

**Edge Cases:**
- ✅ No budget set: Chart shows $0
- ✅ Budget exceeded: Only "Spent" shows, "Remaining" is 0
- ✅ No expenses: Full budget shows as "Remaining"

---

### 11. Form Validation

**Budget Form:**
- ✅ Amount must be positive
- ✅ Amount must be decimal (e.g., 2000.50)
- ✅ Month must be selected

**Expense Form:**
- ✅ Date is required
- ✅ Amount must be positive
- ✅ Amount must be decimal
- ✅ Category must be selected
- ✅ Note is optional

**Test Invalid Inputs:**
- Try negative amount: Should show error
- Try zero amount: Should show error
- Try text in amount field: Should show error

---

### 12. Messages System

**What to Check:**
- ✅ Success messages appear in green
- ✅ Error messages appear in red
- ✅ Messages auto-hide after 5 seconds
- ✅ Messages fade out smoothly

---

## 🎯 Complete Test Scenario

### Full Workflow Test:

1. **Register** → `testuser3` / `test3@example.com` / `SecurePass123!`
2. **Login** → Redirected to dashboard
3. **Set Budget** → $2500 for current month
4. **Add Expenses:**
   - $1200 - Rent - "Monthly rent payment"
   - $300 - Groceries - "Costco shopping"
   - $50 - Food - "Pizza night"
   - $100 - Utilities - "Internet bill"
   - $80 - Travel - "Uber rides"
5. **Verify Calculations:**
   - Total Spent: $1730
   - Remaining: $770
6. **Check Chart:** Shows ~69% spent (red), ~31% remaining (green)
7. **Delete Expense:** Delete the $50 Food expense
8. **Verify Update:**
   - Total Spent: $1680
   - Remaining: $820
   - Chart updates
9. **Logout** → Redirected to login
10. **Login Again** → All data persists

---

## 🐛 Common Issues & Solutions

### Issue: Chart not showing
**Solution:** Check browser console for errors. Ensure Chart.js CDN is loading.

### Issue: Expenses not appearing
**Solution:** Check that date is in current month. Only current month expenses show.

### Issue: Budget not saving
**Solution:** Ensure amount is positive and month is selected.

### Issue: Can't delete expense
**Solution:** Ensure you're logged in and it's your expense.

### Issue: Calculations wrong
**Solution:** Refresh page. Calculations update on page load.

---

## 📊 Expected Dashboard Appearance

```
┌─────────────────────────────────────────────────────────┐
│  💰 BudgetWise          Hello, testuser!  [Logout]     │
└─────────────────────────────────────────────────────────┘

┌──────────────────────────┬──────────────────────────────┐
│ 📊 Set Monthly Budget    │ 📈 Budget Overview           │
│ [Month Dropdown]         │ Monthly Budget: $2000.00     │
│ [Amount Input]           │ Total Spent: $1460.00        │
│ [Save Budget]            │ Remaining: $540.00           │
│                          │                              │
│ Current Budget: $2000    │      [Donut Chart]           │
│ Remaining: $540          │                              │
├──────────────────────────┼──────────────────────────────┤
│ ➕ Add Daily Expense     │ 📋 All Expenses This Month   │
│ [Date]                   │ 🛒 Groceries    $50.00  🗑️   │
│ [Amount]                 │ 🏠 Rent         $1200.00 🗑️  │
│ [Category]               │ 🍔 Food         $30.00   🗑️  │
│ [Note]                   │ ✈️ Travel       $100.00  🗑️  │
│ [Add Expense]            │ 💡 Utilities    $80.00   🗑️  │
├──────────────────────────┤                              │
│ 📅 Today's Expenses      │                              │
│ 🛒 Groceries    $50  🗑️  │                              │
│ 🍔 Food         $30  🗑️  │                              │
└──────────────────────────┴──────────────────────────────┘
```

---

## ✅ Phase 2 Complete!

All features implemented:
- ✅ User authentication (Phase 1)
- ✅ Password reset with email (Phase 1)
- ✅ Expense management dashboard (Phase 2)
- ✅ Budget tracking (Phase 2)
- ✅ Chart visualization (Phase 2)
- ✅ CRUD operations (Phase 2)
- ✅ User data isolation (Phase 2)
- ✅ Responsive design (Phase 2)

**Next Phase:** AI-based expense forecasting (Phase 3)

---

## 🎓 For Developers

### Database Models:
- `Budget`: user, month, amount, created_at, updated_at
- `Expense`: user, amount, category, note, date, created_at

### Key URLs:
- `/dashboard/` - Main dashboard
- `/set-budget/` - Set/update budget
- `/add-expense/` - Add expense
- `/delete-expense/<id>/` - Delete expense
- `/chart-data/` - JSON API for chart

### Security:
- ✅ LoginRequiredMixin on all views
- ✅ CSRF protection on all forms
- ✅ User ownership validation on delete
- ✅ SQL injection protection (Django ORM)

---

**Happy Testing! 🚀**
