#!/usr/bin/env python
"""
Create a default superuser if no users exist.
Run this after deployment: python create_default_user.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if User.objects.count() == 0:
    print("📝 No users found. Creating default superuser...")
    User.objects.create_superuser(
        username='admin',
        email='admin@traveltribe.com',
        password='admin123'  # Change this after first login!
    )
    print("✅ Default superuser created!")
    print("   Username: admin")
    print("   Password: admin123")
    print("   ⚠️  IMPORTANT: Change this password after first login!")
else:
    print(f"✅ Database has {User.objects.count()} user(s) already.")
