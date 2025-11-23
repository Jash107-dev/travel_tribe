#!/usr/bin/env python
"""
Test script to check media file setup
"""
import os
import django
from django.conf import settings

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

def test_media_setup():
    print("🔍 Testing Media File Setup...")
    print(f"📁 MEDIA_ROOT: {settings.MEDIA_ROOT}")
    print(f"🌐 MEDIA_URL: {settings.MEDIA_URL}")
    
    # Check if media directory exists
    if os.path.exists(settings.MEDIA_ROOT):
        print("✅ Media directory exists")
    else:
        print("❌ Media directory does not exist")
        try:
            os.makedirs(settings.MEDIA_ROOT, exist_ok=True)
            print("✅ Created media directory")
        except Exception as e:
            print(f"❌ Failed to create media directory: {e}")
    
    # Check if media directory is writable
    try:
        test_file = os.path.join(settings.MEDIA_ROOT, 'test_write.txt')
        with open(test_file, 'w') as f:
            f.write('test')
        os.remove(test_file)
        print("✅ Media directory is writable")
    except Exception as e:
        print(f"❌ Media directory is not writable: {e}")
    
    # Check subdirectories
    subdirs = ['trip_images', 'trip_gallery', 'trip_photos', 'profile_pics', 'chat_media']
    for subdir in subdirs:
        subdir_path = os.path.join(settings.MEDIA_ROOT, subdir)
        if os.path.exists(subdir_path):
            print(f"✅ {subdir} directory exists")
        else:
            try:
                os.makedirs(subdir_path, exist_ok=True)
                print(f"✅ Created {subdir} directory")
            except Exception as e:
                print(f"❌ Failed to create {subdir} directory: {e}")

if __name__ == '__main__':
    test_media_setup()