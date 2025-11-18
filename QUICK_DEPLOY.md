# 🚀 Quick Deploy - Just Run These Commands

## Step 1: Test Locally (Optional but Recommended)
```bash
python manage.py collectstatic --no-input
python manage.py runserver
```
Visit: http://127.0.0.1:8000 - Should look perfect!

## Step 2: Deploy to Render
```bash
git add .
git commit -m "Fix static files and add creator credit"
git push origin main
```

## Step 3: Wait 2-3 Minutes
Render will automatically:
- Install whitenoise
- Collect static files
- Deploy your site

## Step 4: Done! ✅
Visit: https://travel-tribe-eajn.onrender.com

Your site will be live with all CSS working!

---
**That's it! Just copy-paste these commands.** 🎉
