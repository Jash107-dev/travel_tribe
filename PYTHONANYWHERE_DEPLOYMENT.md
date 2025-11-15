# Deploy Travel Tribe on PythonAnywhere - Complete Guide

## ✅ Why PythonAnywhere?
- ✅ Always FREE (no credit card needed)
- ✅ Django-specific hosting
- ✅ No sleep/downtime
- ✅ Easy setup
- ✅ 512MB storage
- ✅ MySQL database included

---

## 📋 Prerequisites
- PythonAnywhere account (free)
- Your code ready
- GitHub account (optional but recommended)

---

## 🚀 Step-by-Step Deployment

### **Step 1: Sign Up**

1. Go to https://www.pythonanywhere.com
2. Click "Start running Python online in less than a minute!"
3. Choose "Beginner" (FREE) account
4. Sign up with email
5. Verify your email

---

### **Step 2: Upload Your Code**

**Option A: Using Git (Recommended)**

1. Go to PythonAnywhere Dashboard
2. Click "Consoles" → "Bash"
3. Clone your repository:
```bash
git clone https://github.com/yourusername/travel_tribe.git
cd travel_tribe
```

**Option B: Upload ZIP**

1. Zip your project folder
2. Go to "Files" tab
3. Click "Upload a file"
4. Upload and extract

---

### **Step 3: Create Virtual Environment**

In the Bash console:

```bash
# Navigate to your project
cd travel_tribe

# Create virtual environment
mkvirtualenv --python=/usr/bin/python3.10 travel_tribe_env

# Activate it (should auto-activate)
workon travel_tribe_env

# Install requirements
pip install -r requirements.txt

# If requirements.txt doesn't exist:
pip install django pillow
```

---

### **Step 4: Update settings.py**

Add these changes to `travel_tribe/settings.py`:

```python
# At the top
import os

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# Update ALLOWED_HOSTS
ALLOWED_HOSTS = ['yourusername.pythonanywhere.com', 'localhost', '127.0.0.1']

# Database - PythonAnywhere uses MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'yourusername$traveldb',
        'USER': 'yourusername',
        'PASSWORD': 'your-mysql-password',
        'HOST': 'yourusername.mysql.pythonanywhere-services.com',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    }
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'main/static')]

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```

---

### **Step 5: Create MySQL Database**

1. Go to "Databases" tab
2. Under "Create a database", enter: `traveldb`
3. Click "Create"
4. Note your database details:
   - Database name: `yourusername$traveldb`
   - Username: `yourusername`
   - Password: (set a password)
   - Host: `yourusername.mysql.pythonanywhere-services.com`

5. Install MySQL client:
```bash
pip install mysqlclient
```

---

### **Step 6: Run Migrations**

In Bash console:

```bash
cd ~/travel_tribe
workon travel_tribe_env

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Collect static files
python manage.py collectstatic --noinput
```

---

### **Step 7: Configure Web App**

1. Go to "Web" tab
2. Click "Add a new web app"
3. Choose "Manual configuration"
4. Select "Python 3.10"
5. Click "Next"

---

### **Step 8: Configure WSGI File**

1. In "Web" tab, find "Code" section
2. Click on WSGI configuration file link
3. Delete everything and replace with:

```python
import os
import sys

# Add your project directory to the sys.path
path = '/home/yourusername/travel_tribe'
if path not in sys.path:
    sys.path.insert(0, path)

# Set environment variable for Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'travel_tribe.settings'

# Import Django WSGI application
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

**Replace `yourusername` with your actual PythonAnywhere username!**

4. Click "Save"

---

### **Step 9: Configure Virtual Environment**

1. In "Web" tab, find "Virtualenv" section
2. Enter path: `/home/yourusername/.virtualenvs/travel_tribe_env`
3. Click the checkmark

---

### **Step 10: Configure Static Files**

1. In "Web" tab, scroll to "Static files" section
2. Add these mappings:

| URL | Directory |
|-----|-----------|
| `/static/` | `/home/yourusername/travel_tribe/staticfiles` |
| `/media/` | `/home/yourusername/travel_tribe/media` |

3. Click the checkmarks to save

---

### **Step 11: Reload Web App**

1. Scroll to top of "Web" tab
2. Click big green "Reload" button
3. Wait for reload to complete

---

### **Step 12: Test Your Site**

1. Click on your site URL: `https://yourusername.pythonanywhere.com`
2. Your Travel Tribe site should be live! 🎉

---

## 🔧 Troubleshooting

### **Static files not loading:**
```bash
cd ~/travel_tribe
workon travel_tribe_env
python manage.py collectstatic --noinput
```
Then reload web app.

### **500 Internal Server Error:**
1. Check error log in "Web" tab → "Log files" → "Error log"
2. Common issues:
   - Wrong database credentials
   - Missing packages in requirements.txt
   - Wrong paths in WSGI file

### **Database connection error:**
- Verify database name: `yourusername$traveldb`
- Check password is correct
- Ensure mysqlclient is installed

### **Import errors:**
```bash
workon travel_tribe_env
pip install -r requirements.txt
```

---

## 📝 Important Notes

### **Free Account Limits:**
- 512MB disk space
- 1 web app
- 100 seconds CPU time/day
- No custom domain (use subdomain)

### **Updating Your Code:**

**Via Git:**
```bash
cd ~/travel_tribe
git pull origin main
workon travel_tribe_env
python manage.py migrate
python manage.py collectstatic --noinput
```
Then reload web app.

**Via Files:**
1. Upload new files in "Files" tab
2. Reload web app

### **Database Backups:**
1. Go to "Databases" tab
2. Click "Download" next to your database
3. Save the SQL file

---

## 🎯 Quick Checklist

- [ ] Sign up for PythonAnywhere
- [ ] Upload code (Git or ZIP)
- [ ] Create virtual environment
- [ ] Install requirements
- [ ] Create MySQL database
- [ ] Update settings.py with database credentials
- [ ] Run migrations
- [ ] Create superuser
- [ ] Collect static files
- [ ] Configure web app
- [ ] Edit WSGI file
- [ ] Set virtualenv path
- [ ] Configure static files mapping
- [ ] Reload web app
- [ ] Test site

---

## 🌐 Your Site URL

After deployment, your site will be available at:
```
https://yourusername.pythonanywhere.com
```

Replace `yourusername` with your actual PythonAnywhere username.

---

## 💡 Pro Tips

1. **Keep DEBUG=False** in production
2. **Use environment variables** for sensitive data
3. **Regular backups** of database
4. **Monitor error logs** regularly
5. **Update code** via Git for easy deployment

---

## 📞 Need Help?

- PythonAnywhere Forums: https://www.pythonanywhere.com/forums/
- PythonAnywhere Help: https://help.pythonanywhere.com/
- Django Docs: https://docs.djangoproject.com/

---

## 🎉 Congratulations!

Your Travel Tribe project is now live on PythonAnywhere!

**Next Steps:**
1. Test all features
2. Create some test trips
3. Share with friends
4. Monitor error logs
5. Keep your code updated

Happy deploying! 🚀
