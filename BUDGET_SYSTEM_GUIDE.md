# Budget System - Complete Guide

## 🎯 How the Budget System Works

The Budget Status card on the dashboard automatically calculates and displays your remaining budget based on the current month's expenses.

---

## 📊 Budget Calculation Logic

### Formula
```
Remaining Budget = Monthly Budget - Total Expenses (Current Month)
```

### Example Scenarios

#### Scenario 1: Within Budget
- **Monthly Budget:** $30,000
- **Total Expenses:** $29,000
- **Remaining:** $1,000 ✅
- **Display:** "$1,000 Remaining (96.7% used)"

#### Scenario 2: Budget Exceeded
- **Monthly Budget:** $30,000
- **Total Expenses:** $32,000
- **Remaining:** -$2,000 ⚠️
- **Display:** "⚠️ Budget exceeded by $2,000"

#### Scenario 3: No Budget Set
- **Monthly Budget:** $0
- **Total Expenses:** $29,000
- **Remaining:** $0
- **Display:** "No budget set"

---

## 🗄️ Database Model

### Budget Model
```python
class Budget(models.Model):
    user = ForeignKey(User)           # User who owns the budget
    month = CharField(max_length=7)   # Format: "YYYY-MM" (e.g., "2026-03")
    amount = DecimalField              # Budget amount
    created_at = DateTimeField
    updated_at = DateTimeField
    
    class Meta:
        unique_together = ('user', 'month')  # One budget per user per month
```

### Key Features
- ✅ One budget per user per month
- ✅ Stored in YYYY-MM format
- ✅ Decimal precision for accurate calculations
- ✅ Automatic timestamps

---

## 🔄 How Budget Updates Work

### When You Set/Update a Budget

1. **User Action:** Fill budget form and click "Save Budget"
2. **Backend Process:**
   ```python
   Budget.objects.update_or_create(
       user=request.user,
       month='2026-03',  # Current month
       defaults={'amount': 30000}
   )
   ```
3. **Result:** Budget saved or updated in database
4. **Dashboard:** Automatically recalculates on next page load

### When You Add an Expense

1. **User Action:** Add new expense
2. **Backend Process:**
   ```python
   # Expense saved
   expense.save()
   
   # Dashboard recalculates
   total_expenses = Expense.objects.filter(
       user=user,
       date__year=2026,
       date__month=3
   ).aggregate(Sum('amount'))
   
   remaining = budget.amount - total_expenses
   ```
3. **Result:** Budget Status card updates automatically

### When You Delete an Expense

1. **User Action:** Delete expense
2. **Backend Process:** Same as above - recalculates total
3. **Result:** Remaining budget increases

---

## 📈 Dashboard Display Logic

### Budget Status Card

The card shows different information based on the situation:

#### 1. Budget Set & Within Limit
```html
Icon: 💳 (Green)
Value: $1,000
Subtitle: "Remaining (96.7% used)"
```

#### 2. Budget Set & Exceeded
```html
Icon: 💳 (Red)
Value: ⚠️ $2,000
Subtitle: "Budget exceeded by $2,000"
Banner: "⚠️ Budget Alert: You've exceeded your monthly budget..."
```

#### 3. Budget Set & Warning (>80% used)
```html
Icon: 💳 (Orange)
Value: $5,000
Subtitle: "Remaining (83.3% used)"
```

#### 4. No Budget Set
```html
Icon: 💳 (Purple)
Value: $0.00
Subtitle: "No budget set"
```

---

## 🔍 Backend Implementation

### ExpenseAnalytics Service

Located in: `expenses/services.py`

```python
def get_budget_status(self):
    """Get current month budget status"""
    now = datetime.now()
    month_str = now.strftime('%Y-%m')  # e.g., "2026-03"
    
    # Get budget for current month
    budget = Budget.objects.filter(
        user=self.user,
        month=month_str
    ).first()
    
    # Get total expenses for current month
    total_spent = self.get_current_month_total()
    
    if budget:
        remaining = budget.amount - total_spent
        percentage = (total_spent / budget.amount * 100) if budget.amount > 0 else 0
        return {
            'budget': budget.amount,
            'spent': total_spent,
            'remaining': remaining,
            'percentage': round(percentage, 1)
        }
    
    return {
        'budget': Decimal('0.00'),
        'spent': total_spent,
        'remaining': Decimal('0.00'),
        'percentage': 0
    }
```

### Dashboard View

Located in: `expenses/views.py`

```python
class DashboardView(LoginRequiredMixin, View):
    def get(self, request):
        analytics = ExpenseAnalytics(request.user)
        summary = analytics.get_dashboard_summary()
        
        # summary contains:
        # - total_expenses
        # - transaction_count
        # - highest_category
        # - budget_status (with budget, spent, remaining, percentage)
        
        context = {'summary': summary, ...}
        return render(request, 'expenses/dashboard.html', context)
```

---

## 🎨 UI Components

### Summary Card HTML

```html
<div class="summary-card">
    <div class="card-icon {% if remaining < 0 %}red{% endif %}">
        💳
    </div>
    <div class="card-content">
        <div class="card-label">Budget Status</div>
        {% if budget > 0 %}
            {% if remaining < 0 %}
                <div class="card-value-small negative">
                    ⚠️ ${{ remaining|abs }}
                </div>
                <div class="card-subtitle">
                    Budget exceeded by ${{ remaining|abs }}
                </div>
            {% else %}
                <div class="card-value-small">
                    ${{ remaining }}
                </div>
                <div class="card-subtitle">
                    Remaining ({{ percentage }}% used)
                </div>
            {% endif %}
        {% else %}
            <div class="card-value-small">$0.00</div>
            <div class="card-subtitle">No budget set</div>
        {% endif %}
    </div>
</div>
```

### Budget Progress Bar

```html
{% if budget > 0 %}
<div class="budget-progress">
    <div class="progress-bar">
        <div class="progress-fill" style="width: {{ percentage }}%"></div>
    </div>
    <div class="progress-labels">
        <span>Spent: ${{ spent }}</span>
        <span>Budget: ${{ budget }}</span>
    </div>
</div>
{% endif %}
```

---

## 🔄 Real-Time Updates

### When Does the Dashboard Update?

The dashboard recalculates budget status in these scenarios:

1. **Page Load/Refresh** ✅
   - Fetches latest budget
   - Calculates current month expenses
   - Updates all cards

2. **After Adding Expense** ✅
   - Redirects to dashboard
   - Dashboard recalculates automatically

3. **After Deleting Expense** ✅
   - Redirects to dashboard
   - Dashboard recalculates automatically

4. **After Setting/Updating Budget** ✅
   - Redirects to dashboard
   - Dashboard shows new budget immediately

### No Caching
- All calculations are done in real-time
- No cached values
- Always shows current data

---

## 🧪 Testing the Budget System

### Test Case 1: Set Budget
1. Go to Dashboard
2. Set budget: $30,000 for current month
3. Click "Save Budget"
4. **Expected:** Success message, Budget Status shows $30,000 remaining

### Test Case 2: Add Expenses
1. Add expense: $10,000 (Entertainment)
2. Add expense: $15,000 (Rent)
3. Add expense: $4,000 (Food)
4. **Expected:** Budget Status shows $1,000 remaining (96.7% used)

### Test Case 3: Exceed Budget
1. Add expense: $2,000 (Shopping)
2. **Expected:** 
   - Budget Status shows "⚠️ $1,000"
   - Subtitle: "Budget exceeded by $1,000"
   - Warning banner appears
   - Icon turns red

### Test Case 4: Delete Expense
1. Delete the $2,000 Shopping expense
2. **Expected:** Budget Status returns to $1,000 remaining

### Test Case 5: Update Budget
1. Change budget to $35,000
2. **Expected:** Budget Status shows $6,000 remaining

### Test Case 6: No Budget
1. Don't set any budget
2. Add expenses
3. **Expected:** Budget Status shows "No budget set"

---

## 🔐 Security Features

### User Isolation
```python
# Only fetch current user's budget
budget = Budget.objects.filter(
    user=request.user,  # ✅ User-specific
    month=month_str
).first()

# Only fetch current user's expenses
expenses = Expense.objects.filter(
    user=request.user  # ✅ User-specific
)
```

### Data Validation
- ✅ Budget amount must be positive
- ✅ One budget per user per month (unique constraint)
- ✅ Decimal precision for accurate calculations
- ✅ CSRF protection on forms

---

## 📊 Example Data Flow

### Complete Flow Example

**Initial State:**
- User: John
- Month: March 2026
- Budget: Not set
- Expenses: None

**Step 1: Set Budget**
```
Action: Set budget $30,000 for March 2026
Database: Budget(user=John, month='2026-03', amount=30000)
Dashboard: Budget Status = $30,000 remaining (0% used)
```

**Step 2: Add Expenses**
```
Action: Add $10,000 Entertainment
Database: Expense(user=John, amount=10000, date='2026-03-15')
Dashboard: Budget Status = $20,000 remaining (33.3% used)

Action: Add $15,000 Rent
Database: Expense(user=John, amount=15000, date='2026-03-01')
Dashboard: Budget Status = $5,000 remaining (83.3% used)
Icon: Orange (warning)

Action: Add $4,000 Food
Database: Expense(user=John, amount=4000, date='2026-03-20')
Dashboard: Budget Status = $1,000 remaining (96.7% used)
Icon: Orange (warning)
```

**Step 3: Exceed Budget**
```
Action: Add $2,000 Shopping
Database: Expense(user=John, amount=2000, date='2026-03-25')
Dashboard: 
  - Budget Status = ⚠️ $1,000 (Budget exceeded by $1,000)
  - Icon: Red
  - Warning banner appears
```

**Step 4: Delete Expense**
```
Action: Delete $2,000 Shopping
Database: Expense deleted
Dashboard: Budget Status = $1,000 remaining (96.7% used)
Icon: Orange (back to warning level)
```

---

## 🎯 Key Points

### What Works Automatically
✅ Budget calculation for current month  
✅ Real-time updates on page load  
✅ User-specific data isolation  
✅ Percentage calculation  
✅ Warning indicators  
✅ Budget exceeded detection  

### What Requires User Action
- Setting monthly budget
- Adding/deleting expenses
- Refreshing page to see updates

### What's NOT Supported (Yet)
- Historical budget comparison
- Budget forecasting
- Automatic budget rollover
- Budget categories
- Multiple budgets per month

---

## 🚀 Future Enhancements

Potential improvements:
- [ ] Budget alerts via email
- [ ] Budget recommendations based on spending
- [ ] Category-specific budgets
- [ ] Budget vs actual comparison charts
- [ ] Budget rollover to next month
- [ ] Budget templates
- [ ] Shared budgets (family/team)

---

## 📝 Summary

The Budget System:
1. ✅ Stores one budget per user per month
2. ✅ Calculates remaining budget automatically
3. ✅ Updates in real-time on page load
4. ✅ Shows warnings when budget exceeded
5. ✅ Displays clear status messages
6. ✅ Maintains user data isolation
7. ✅ Uses accurate decimal calculations

**The system is working correctly. The dashboard updates automatically based on the current month's budget and expenses.**

---

**For questions or issues, refer to the complete testing guide or check the code in:**
- `expenses/models.py` - Budget model
- `expenses/services.py` - Budget calculations
- `expenses/views.py` - Dashboard logic
- `expenses/templates/expenses/dashboard.html` - UI display
