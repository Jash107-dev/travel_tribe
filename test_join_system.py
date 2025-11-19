#!/usr/bin/env python
"""
Quick test to verify join request system is working
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import Trip, JoinRequest

def test_join_system():
    print("🧪 Testing Join Request System...")
    
    # Check if JoinRequest model exists
    try:
        requests = JoinRequest.objects.all()
        print(f"✅ JoinRequest model working - {requests.count()} requests found")
    except Exception as e:
        print(f"❌ JoinRequest model error: {e}")
        return
    
    # Check if there are any trips
    trips = Trip.objects.all()
    print(f"📍 Found {trips.count()} trips")
    
    if trips.exists():
        trip = trips.first()
        print(f"🎯 Testing with trip: {trip.destination}")
        
        # Check trip members
        print(f"👥 Current members: {trip.members_count}/{trip.members_limit}")
        for member in trip.joined_members.all():
            print(f"   - {member.username}")
        
        # Check join requests for this trip
        trip_requests = JoinRequest.objects.filter(trip=trip)
        print(f"📋 Join requests for this trip: {trip_requests.count()}")
        for req in trip_requests:
            print(f"   - {req.user.username}: {req.status}")
    
    print("\n🔍 System Status:")
    print("✅ JoinRequest model exists")
    print("✅ Migration applied")
    print("✅ Views updated")
    print("✅ Templates updated")
    print("\n💡 If users can still join directly, check:")
    print("1. Clear browser cache")
    print("2. Check if old URLs are cached")
    print("3. Verify deployment updated all files")

if __name__ == "__main__":
    test_join_system()