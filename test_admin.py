#!/usr/bin/env python
"""
Test script to check admin access
"""
import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

from django.contrib.auth.models import User
from django.test import Client

def test_admin_access():
    print("🔍 Testing Admin Access...")
    
    # Check admin user
    try:
        admin_user = User.objects.get(username='Jashwanth')
        print(f"✅ Admin user found: {admin_user.username}")
        print(f"   - Is superuser: {admin_user.is_superuser}")
        print(f"   - Is staff: {admin_user.is_staff}")
        print(f"   - Is active: {admin_user.is_active}")
    except User.DoesNotExist:
        print("❌ Admin user not found")
        return
    
    # Test client
    client = Client()
    
    # Test admin login page
    response = client.get('/admin/')
    print(f"📄 Admin page status: {response.status_code}")
    
    if response.status_code == 200:
        print("✅ Admin page accessible")
    else:
        print(f"❌ Admin page error: {response.status_code}")
    
    # Test login
    login_response = client.post('/admin/login/', {
        'username': 'Jashwanth',
        'password': 'Jash@2289',
        'next': '/admin/'
    })
    
    print(f"🔐 Login response: {login_response.status_code}")
    
    if login_response.status_code == 302:  # Redirect after successful login
        print("✅ Login successful")
    else:
        print(f"❌ Login failed: {login_response.status_code}")

if __name__ == '__main__':
    test_admin_access()