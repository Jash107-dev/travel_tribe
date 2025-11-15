# 🚀 Quick Start - PythonAnywhere Deployment

## 5-Minute Setup Guide

### 1️⃣ Sign Up (2 minutes)
- Go to https://www.pythonanywhere.com
- Click "Start running Python online"
- Choose FREE "Beginner" account
- Sign up and verify email

### 2️⃣ Upload Code (1 minute)
**Bash Console:**
```bash
git clone https://github.com/yourusername/travel_tribe.git
cd travel_tribe
```

### 3️⃣ Setup Environment (1 minute)
```bash
mkvirtualenv --python=/usr/bin/python3.10 myenv
pip install django pillow mysqlclient
```

### 4️⃣ Create Database (30 seconds)
- Go to "Databases" tab
- Create database: `traveldb`
- Set password

### 5️⃣ Configure Web App (1 minute)
- "Web" tab → "Add new web app"
- Manual configuration → Python 3.10
- Edit WSGI file (copy from full guide)
- Set virtualenv path
- Add static files mapping

### 6️⃣ Deploy (30 seconds)
```bash
python manage.py migrate
python manage.py collectstatic
```
Click "Reload" button

### ✅ Done!
Visit: `https://yourusername.pythonanywhere.com`

---

## 📖 Full Guide
See `PYTHONANYWHERE_DEPLOYMENT.md` for detailed instructions.

## ⚡ Key Points
- ✅ Always FREE
- ✅ No credit card
- ✅ No downtime
- ✅ MySQL included
- ✅ 512MB storage

## 🆘 Common Issues

**Static files not showing?**
```bash
python manage.py collectstatic --noinput
```

**500 Error?**
Check error log in Web tab

**Database error?**
Verify credentials in settings.py

---

Your site will be live at:
**https://yourusername.pythonanywhere.com**

🎉 Happy deploying!
