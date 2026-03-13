# Gmail SMTP Setup Instructions

## ⚠️ IMPORTANT: You Need a Gmail App Password

Gmail doesn't allow regular passwords for third-party apps. You must create an **App Password**.

---

## Step-by-Step: Create Gmail App Password

### 1. Enable 2-Step Verification (Required)

1. Go to your Google Account: https://myaccount.google.com/
2. Click **Security** in the left menu
3. Under "How you sign in to Google", click **2-Step Verification**
4. Follow the steps to enable it (you'll need your phone)

### 2. Create App Password

1. After enabling 2-Step Verification, go back to **Security**
2. Under "How you sign in to Google", click **App passwords**
   - Or visit directly: https://myaccount.google.com/apppasswords
3. You may need to sign in again
4. Click **Select app** → Choose "Mail"
5. Click **Select device** → Choose "Other (Custom name)"
6. Type: `BudgetWise Django App`
7. Click **Generate**
8. **Copy the 16-character password** (it looks like: `abcd efgh ijkl mnop`)

### 3. Update Your .env File

Open your `.env` file and replace `your_app_password_here` with the App Password:

```env
EMAIL_HOST_PASSWORD=abcdefghijklmnop
```

**Note:** Remove all spaces from the App Password!

---

## Current Configuration

Your email is configured as:
- **Email:** y23cd148.ai@gmail.com
- **SMTP Server:** smtp.gmail.com
- **Port:** 587
- **TLS:** Enabled

---

## Testing the Email

1. **Update the App Password** in `.env` file
2. **Restart the Django server**
3. Go to: http://127.0.0.1:8000/accounts/password-reset/
4. Enter an email address of a registered user
5. Check your **actual Gmail inbox** for the reset email

---

## Troubleshooting

### Error: "Username and Password not accepted"

**Solution:** You're using your regular Gmail password. You MUST use an App Password.

### Error: "2-Step Verification is not enabled"

**Solution:** Enable 2-Step Verification first (see Step 1 above)

### Error: "SMTPAuthenticationError"

**Solutions:**
1. Make sure you copied the App Password correctly (no spaces)
2. Verify 2-Step Verification is enabled
3. Try generating a new App Password

### Still Not Working?

**Alternative: Use Console Backend for Development**

If you can't set up Gmail, you can switch back to console emails:

In `budgetwise/settings.py`, change:
```python
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
```

Emails will print to the terminal instead.

---

## Security Notes

- ✅ App Passwords are safer than your main password
- ✅ You can revoke App Passwords anytime
- ✅ Never share your App Password
- ✅ Don't commit `.env` file to Git (it's in .gitignore)

---

## Quick Links

- Google Account Security: https://myaccount.google.com/security
- App Passwords: https://myaccount.google.com/apppasswords
- 2-Step Verification: https://myaccount.google.com/signinoptions/two-step-verification

---

**Once you've created the App Password and updated `.env`, restart the server and test!**
