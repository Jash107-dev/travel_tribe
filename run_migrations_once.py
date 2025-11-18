#!/usr/bin/env python
"""
One-time script to run migrations and create admin user.
This will be triggered automatically on first request.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

from django.core.management import call_command
from django.contrib.auth import get_user_model

print("=" * 60)
print("RUNNING MIGRATIONS")
print("=" * 60)

try:
    call_command('migrate', '--no-input', verbosity=2)
    print("✅ Migrations completed successfully!")
    
    User = get_user_model()
    if User.objects.count() == 0:
        print("\n" + "=" * 60)
        print("CREATING DEFAULT ADMIN USER")
        print("=" * 60)
        User.objects.create_superuser(
            username='admin',
            email='admin@traveltribe.com',
            password='admin123'
        )
        print("✅ Admin user created!")
        print("   Username: admin")
        print("   Password: admin123")
    else:
        print(f"\n✅ Database has {User.objects.count()} user(s)")
        
except Exception as e:
    print(f"❌ Error: {e}")
    raise

print("\n" + "=" * 60)
print("SETUP COMPLETE!")
print("=" * 60)
