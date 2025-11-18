# Create Superuser on Render

After deployment completes, you need to create an admin user.

## Option 1: Using Render Shell (Recommended)

1. Go to Render Dashboard
2. Click on your service "travel-tribe"
3. Click "Shell" tab
4. Run this command:
```bash
python manage.py createsuperuser
```
5. Enter:
   - Username: Jashwanth
   - Email: (your email)
   - Password: (your password)

## Option 2: Using Django Admin

1. Visit: https://travel-tribe-eajn.onrender.com/admin/
2. You won't be able to login yet (no users)
3. Use Option 1 first to create a user

## After Creating Superuser

You can:
- Login at: https://travel-tribe-eajn.onrender.com/
- Access admin at: https://travel-tribe-eajn.onrender.com/admin/
- Create trips, manage users, etc.

Your site will be FULLY WORKING with:
✅ PostgreSQL database
✅ All CSS styling
✅ Static files
✅ Media uploads
✅ Everything! 🎉
