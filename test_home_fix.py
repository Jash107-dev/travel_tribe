#!/usr/bin/env python
"""
Quick test to verify the home view fix works
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

from django.test import RequestFactory
from main.views import home

def test_home_view():
    """Test that home view works without errors"""
    factory = RequestFactory()
    request = factory.get('/home/')
    
    try:
        response = home(request)
        print(f"✅ Home view returned status: {response.status_code}")
        
        if response.status_code == 200:
            print("✅ SUCCESS: Home page loads correctly!")
            return True
        else:
            print(f"⚠️  WARNING: Unexpected status code: {response.status_code}")
            return False
            
    except Exception as e:
        print(f"❌ ERROR: {str(e)}")
        return False

if __name__ == '__main__':
    print("🧪 Testing home view fix...")
    print("-" * 50)
    success = test_home_view()
    print("-" * 50)
    
    if success:
        print("\n✅ All tests passed! Ready to deploy.")
    else:
        print("\n❌ Tests failed. Check the errors above.")
