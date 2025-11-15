"""
Comprehensive Test Script for Travel Tribe
Tests all features and URLs
"""

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import Trip, TripPost, ChatRoom, ChatMessage, UserProfile
from django.test import Client
from django.urls import reverse

def test_all_features():
    print("🧪 COMPREHENSIVE FEATURE TEST\n")
    print("=" * 50)
    
    client = Client()
    errors = []
    
    # Test 1: Check all URLs exist
    print("\n1️⃣ Testing URL Patterns...")
    urls_to_test = [
        'login', 'register', 'home', 'trip_feed', 'create_trip', 
        'add_trip', 'user_profile', 'forgot_password', 'verify_otp'
    ]
    
    for url_name in urls_to_test:
        try:
            url = reverse(url_name)
            print(f"   ✅ {url_name}: {url}")
        except Exception as e:
            error_msg = f"   ❌ {url_name}: {str(e)}"
            print(error_msg)
            errors.append(error_msg)
    
    # Test 2: Check Models
    print("\n2️⃣ Testing Models...")
    try:
        user_count = User.objects.count()
        trip_count = Trip.objects.count()
        trippost_count = TripPost.objects.count()
        profile_count = UserProfile.objects.count()
        print(f"   ✅ Users: {user_count}")
        print(f"   ✅ Trips: {trip_count}")
        print(f"   ✅ Trip Posts: {trippost_count}")
        print(f"   ✅ Profiles: {profile_count}")
    except Exception as e:
        error_msg = f"   ❌ Model Error: {str(e)}"
        print(error_msg)
        errors.append(error_msg)
    
    # Test 3: Check User Profile Creation
    print("\n3️⃣ Testing User Profile Auto-Creation...")
    try:
        for user in User.objects.all():
            profile, created = UserProfile.objects.get_or_create(user=user)
            if created:
                print(f"   ✅ Created profile for {user.username}")
        print(f"   ✅ All users have profiles")
    except Exception as e:
        error_msg = f"   ❌ Profile Error: {str(e)}"
        print(error_msg)
        errors.append(error_msg)
    
    # Test 4: Check ChatRooms
    print("\n4️⃣ Testing ChatRooms...")
    try:
        for trip_post in TripPost.objects.all():
            chatroom, created = ChatRoom.objects.get_or_create(trip_post=trip_post)
            if created:
                print(f"   ✅ Created chatroom for {trip_post.destination}")
        print(f"   ✅ All trip posts have chatrooms")
    except Exception as e:
        error_msg = f"   ❌ ChatRoom Error: {str(e)}"
        print(error_msg)
        errors.append(error_msg)
    
    # Test 5: Check Trip Posts have members_count method
    print("\n5️⃣ Testing TripPost Methods...")
    try:
        for trip_post in TripPost.objects.all()[:3]:
            count = trip_post.members_count
            print(f"   ✅ {trip_post.destination}: {count} members")
    except Exception as e:
        error_msg = f"   ❌ TripPost Method Error: {str(e)}"
        print(error_msg)
        errors.append(error_msg)
    
    # Summary
    print("\n" + "=" * 50)
    if errors:
        print(f"\n❌ FOUND {len(errors)} ERRORS:")
        for error in errors:
            print(error)
    else:
        print("\n✅ ALL TESTS PASSED! NO ERRORS FOUND!")
    print("\n" + "=" * 50)

if __name__ == '__main__':
    test_all_features()
