# Travel Tribe - Free Deployment Guide

## Option 1: Render (Recommended) ⭐

### Prerequisites
- GitHub account
- Your code pushed to GitHub

### Steps:

1. **Add gunicorn to requirements.txt**
   ```bash
   pip install gunicorn dj-database-url psycopg2-binary
   pip freeze > requirements.txt
   ```

2. **Update settings.py**
   Add at the top:
   ```python
   import os
   import dj_database_url
   ```
   
   Update:
   ```python
   SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here')
   DEBUG = os.environ.get('DEBUG', 'False') == 'True'
   ALLOWED_HOSTS = ['*']  # Update with your domain
   
   # Database
   DATABASES = {
       'default': dj_database_url.config(
           default='sqlite:///db.sqlite3',
           conn_max_age=600
       )
   }
   
   # Static files
   STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
   STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
   ```

3. **Make build.sh executable**
   ```bash
   chmod +x build.sh
   ```

4. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Prepare for deployment"
   git push
   ```

5. **Deploy on Render**
   - Go to https://render.com
   - Sign up with GitHub
   - Click "New +" → "Web Service"
   - Connect your repository
   - Settings:
     - Name: travel-tribe
     - Build Command: `./build.sh`
     - Start Command: `gunicorn travel_tribe.wsgi:application`
   - Click "Create Web Service"

6. **Add PostgreSQL Database (Optional)**
   - In Render dashboard, click "New +" → "PostgreSQL"
   - Connect it to your web service
   - Render will auto-configure DATABASE_URL

---

## Option 2: PythonAnywhere

### Steps:

1. **Sign up at https://www.pythonanywhere.com**

2. **Upload your code**
   - Use Git: `git clone your-repo-url`
   - Or upload zip file

3. **Create virtual environment**
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 myenv
   pip install -r requirements.txt
   ```

4. **Configure Web App**
   - Go to Web tab
   - Add new web app
   - Choose Django
   - Set source code path
   - Set WSGI file path

5. **Configure Static Files**
   - URL: /static/
   - Directory: /home/yourusername/travel_tribe/staticfiles/

6. **Run migrations**
   ```bash
   python manage.py migrate
   python manage.py collectstatic
   ```

---

## Option 3: Railway

### Steps:

1. **Go to https://railway.app**

2. **Sign up with GitHub**

3. **New Project → Deploy from GitHub**

4. **Select your repository**

5. **Add PostgreSQL**
   - Click "New" → "Database" → "PostgreSQL"
   - Railway auto-configures DATABASE_URL

6. **Add environment variables**
   - SECRET_KEY
   - DEBUG=False

7. **Deploy automatically**

---

## Important Notes:

### Security:
- Never commit SECRET_KEY to GitHub
- Set DEBUG=False in production
- Update ALLOWED_HOSTS with your domain

### Media Files:
For user uploads, use:
- **Cloudinary** (free tier)
- **AWS S3** (free tier)
- **Render Disks** (paid)

### Database:
- SQLite works for small projects
- PostgreSQL recommended for production
- All platforms offer free PostgreSQL

### Custom Domain:
- Render: Free custom domain support
- PythonAnywhere: Paid plans only
- Railway: Free custom domain

---

## Troubleshooting:

### Static files not loading:
```bash
python manage.py collectstatic --no-input
```

### Database errors:
```bash
python manage.py migrate
```

### Module not found:
```bash
pip install -r requirements.txt
```

---

## Free Tier Limits:

| Platform | Storage | Bandwidth | Database | Sleep |
|----------|---------|-----------|----------|-------|
| Render | 512MB | 100GB/mo | 1GB PostgreSQL | After 15min inactive |
| PythonAnywhere | 512MB | Limited | MySQL | No sleep |
| Railway | 1GB | 100GB/mo | 1GB PostgreSQL | $5 credit/mo |

---

## Recommended: Render

**Why?**
- Easiest setup
- Auto-deploys from GitHub
- Free PostgreSQL
- Free SSL certificate
- Good performance

**Deploy Now:**
1. Push code to GitHub
2. Sign up at render.com
3. Connect repo
4. Click deploy
5. Done! 🎉

Your app will be live at: `https://your-app-name.onrender.com`
