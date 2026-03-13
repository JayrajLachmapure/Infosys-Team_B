# Complete Setup Guide for BudgetWise on Windows

## Prerequisites Checklist

- [ ] Python 3.10+ installed
- [ ] PostgreSQL installed
- [ ] Internet connection for downloading packages

---

## Step 1: Install PostgreSQL on Windows

### Option A: Using Official Installer (Recommended)

1. **Download PostgreSQL**
   - Visit: https://www.postgresql.org/download/windows/
   - Click "Download the installer"
   - Choose the latest version (PostgreSQL 16.x recommended)
   - Download the Windows x86-64 installer

2. **Run the Installer**
   - Double-click the downloaded `.exe` file
   - Click "Next" on the welcome screen

3. **Installation Directory**
   - Keep default: `C:\Program Files\PostgreSQL\16`
   - Click "Next"

4. **Select Components**
   - Check all boxes:
     - [x] PostgreSQL Server
     - [x] pgAdmin 4 (GUI tool)
     - [x] Stack Builder
     - [x] Command Line Tools
   - Click "Next"

5. **Data Directory**
   - Keep default: `C:\Program Files\PostgreSQL\16\data`
   - Click "Next"

6. **Set Password** ⚠️ IMPORTANT
   - Enter a password for the `postgres` superuser
   - **Remember this password!** You'll need it later
   - Example: `postgres123` (use something secure)
   - Confirm the password
   - Click "Next"

7. **Port**
   - Keep default: `5432`
   - Click "Next"

8. **Locale**
   - Keep default locale
   - Click "Next"

9. **Complete Installation**
   - Review settings
   - Click "Next" to install
   - Wait for installation (2-5 minutes)
   - Uncheck "Stack Builder" at the end
   - Click "Finish"

### Option B: Using Chocolatey (If you have it)

```powershell
choco install postgresql
```

---

## Step 2: Verify PostgreSQL Installation

1. **Open Command Prompt or PowerShell**

2. **Check PostgreSQL version**
   ```cmd
   psql --version
   ```
   Should show: `psql (PostgreSQL) 16.x`

3. **If command not found**, add to PATH:
   - Search "Environment Variables" in Windows
   - Click "Environment Variables"
   - Under "System variables", find "Path"
   - Click "Edit"
   - Click "New"
   - Add: `C:\Program Files\PostgreSQL\16\bin`
   - Click "OK" on all windows
   - **Restart your terminal**

---

## Step 3: Create Database for BudgetWise

### Method 1: Using pgAdmin (GUI - Easier)

1. **Open pgAdmin 4**
   - Search "pgAdmin" in Windows Start menu
   - Launch pgAdmin 4

2. **Connect to Server**
   - Expand "Servers" in left panel
   - Click "PostgreSQL 16"
   - Enter the password you set during installation
   - Check "Save Password" (optional)

3. **Create Database**
   - Right-click "Databases"
   - Select "Create" → "Database"
   - Database name: `budgetwise_db`
   - Owner: `postgres`
   - Click "Save"

4. **Verify**
   - You should see `budgetwise_db` under Databases

### Method 2: Using Command Line

1. **Open Command Prompt as Administrator**

2. **Connect to PostgreSQL**
   ```cmd
   psql -U postgres
   ```
   - Enter your postgres password when prompted

3. **Create Database**
   ```sql
   CREATE DATABASE budgetwise_db;
   ```

4. **Verify Database**
   ```sql
   \l
   ```
   - You should see `budgetwise_db` in the list

5. **Exit**
   ```sql
   \q
   ```

---

## Step 4: Configure BudgetWise Application

1. **Open the `.env` file** in your project root

2. **Update with your PostgreSQL password**
   ```env
   DB_NAME=budgetwise_db
   DB_USER=postgres
   DB_PASSWORD=YOUR_POSTGRES_PASSWORD_HERE
   DB_HOST=localhost
   DB_PORT=5432
   SECRET_KEY=django-insecure-dev-key-change-in-production-12345
   DEBUG=True
   ```
   Replace `YOUR_POSTGRES_PASSWORD_HERE` with the password you set during PostgreSQL installation

3. **Save the file**

---

## Step 5: Set Up Python Virtual Environment

1. **Open PowerShell or Command Prompt** in your project directory

2. **Create virtual environment**
   ```cmd
   python -m venv venv
   ```

3. **Activate virtual environment**
   
   **PowerShell:**
   ```powershell
   .\venv\Scripts\Activate.ps1
   ```
   
   **If you get execution policy error:**
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
   Then try activating again.
   
   **Command Prompt (cmd):**
   ```cmd
   venv\Scripts\activate.bat
   ```

4. **Verify activation**
   - You should see `(venv)` at the start of your command line

---

## Step 6: Install Python Dependencies

```cmd
pip install -r requirements.txt
```

Wait for all packages to install (Django, psycopg2-binary, python-dotenv)

---

## Step 7: Run Database Migrations

1. **Create migration files**
   ```cmd
   python manage.py makemigrations
   ```

2. **Apply migrations to database**
   ```cmd
   python manage.py migrate
   ```
   
   You should see output like:
   ```
   Running migrations:
     Applying contenttypes.0001_initial... OK
     Applying auth.0001_initial... OK
     Applying admin.0001_initial... OK
     ...
   ```

---

## Step 8: Create Admin User (Optional but Recommended)

```cmd
python manage.py createsuperuser
```

Follow the prompts:
- Username: `admin` (or your choice)
- Email: `admin@example.com` (or your email)
- Password: Enter a secure password
- Password (again): Confirm password

---

## Step 9: Run the Application

```cmd
python manage.py runserver
```

You should see:
```
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

---

## Step 10: Test the Application

1. **Open your web browser**

2. **Visit the application**
   - Main page: http://127.0.0.1:8000/
   - Login: http://127.0.0.1:8000/accounts/login/
   - Signup: http://127.0.0.1:8000/accounts/signup/
   - Admin: http://127.0.0.1:8000/admin/

3. **Test Signup**
   - Go to signup page
   - Create a new account:
     - Username: `testuser`
     - Email: `test@example.com`
     - Password: `SecurePass123!`
     - Confirm password: `SecurePass123!`
   - Click "Create Account"

4. **Test Login**
   - You'll be redirected to login
   - Enter your credentials
   - Click "Sign In"
   - You should see the dashboard

5. **Test Admin Panel** (if you created superuser)
   - Visit: http://127.0.0.1:8000/admin/
   - Login with superuser credentials
   - You can see all registered users

---

## Troubleshooting

### PostgreSQL Connection Error

**Error:** `connection to server at "localhost" failed`

**Solutions:**
1. Check if PostgreSQL is running:
   - Open Services (Win + R, type `services.msc`)
   - Find "postgresql-x64-16"
   - Status should be "Running"
   - If not, right-click → Start

2. Verify password in `.env` file matches your PostgreSQL password

3. Check port 5432 is not blocked:
   ```cmd
   netstat -an | findstr 5432
   ```

### Python Module Not Found

**Error:** `ModuleNotFoundError: No module named 'django'`

**Solution:**
```cmd
pip install -r requirements.txt
```

### Virtual Environment Not Activating

**Error:** `cannot be loaded because running scripts is disabled`

**Solution:**
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Port 8000 Already in Use

**Error:** `Error: That port is already in use`

**Solution:**
```cmd
python manage.py runserver 8001
```

### Database Already Exists Error

**Solution:**
Skip database creation, just update `.env` and run migrations

---

## Quick Reference Commands

```cmd
# Activate virtual environment
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver

# Stop server
Ctrl + C

# Deactivate virtual environment
deactivate
```

---

## System Requirements

- **OS:** Windows 10/11
- **Python:** 3.10 or higher
- **PostgreSQL:** 14 or higher
- **RAM:** 4GB minimum
- **Disk Space:** 500MB for PostgreSQL + 100MB for project

---

## Next Steps After Setup

Once everything is running:

1. ✅ Create a test user account
2. ✅ Login and view dashboard
3. ✅ Test logout functionality
4. ✅ Access admin panel
5. ✅ Verify user data in PostgreSQL (using pgAdmin)

---

## Need Help?

- PostgreSQL Documentation: https://www.postgresql.org/docs/
- Django Documentation: https://docs.djangoproject.com/
- pgAdmin Documentation: https://www.pgadmin.org/docs/

---

**You're all set! 🎉**
