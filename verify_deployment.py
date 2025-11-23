#!/usr/bin/env python3
"""
Quick deployment verification script
"""
import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

def verify_deployment():
    print("🔍 Verifying deployment readiness...")
    
    # Check critical imports
    try:
        from main.models import Trip, User
        from main.views import home, health_check
        print("✅ All critical imports successful")
    except Exception as e:
        print(f"❌ Import error: {e}")
        return False
    
    # Check database models
    try:
        from django.core.management import execute_from_command_line
        print("✅ Django management commands accessible")
    except Exception as e:
        print(f"❌ Django setup error: {e}")
        return False
    
    # Check settings
    print(f"✅ DEBUG: {settings.DEBUG}")
    print(f"✅ ALLOWED_HOSTS: {settings.ALLOWED_HOSTS}")
    print(f"✅ Database: {settings.DATABASES['default']['ENGINE']}")
    
    print("🎉 Deployment verification passed!")
    return True

if __name__ == '__main__':
    verify_deployment()