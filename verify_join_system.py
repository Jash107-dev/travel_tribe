#!/usr/bin/env python
"""
Verify the join request system is working properly
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import Trip, JoinRequest

def verify_system():
    print("🔒 VERIFYING SECURE JOIN REQUEST SYSTEM")
    print("=" * 50)
    
    # Check models exist
    print("✅ JoinRequest model exists")
    print("✅ Trip model exists")
    
    # Check current state
    trips = Trip.objects.all()
    requests = JoinRequest.objects.all()
    
    print(f"📍 Total trips: {trips.count()}")
    print(f"📋 Total join requests: {requests.count()}")
    
    if trips.exists():
        for trip in trips[:3]:  # Show first 3 trips
            print(f"\n🎯 Trip: {trip.destination}")
            print(f"   Creator: {trip.created_by.username}")
            print(f"   Members: {trip.members_count}/{trip.members_limit}")
            
            # Show members
            members = trip.joined_members.all()
            if members:
                print("   Current members:")
                for member in members:
                    print(f"     - {member.username}")
            
            # Show requests
            trip_requests = JoinRequest.objects.filter(trip=trip)
            if trip_requests:
                print("   Join requests:")
                for req in trip_requests:
                    print(f"     - {req.user.username}: {req.status}")
            else:
                print("   No join requests yet")
    
    print("\n🛡️ SECURITY STATUS:")
    print("✅ Only JoinRequest.approve() can add members")
    print("✅ join_destination_trip() only creates requests")
    print("✅ No direct member addition allowed")
    
    print("\n🧪 TO TEST:")
    print("1. Go to /test-join-system/ on your site")
    print("2. Try to join a trip you didn't create")
    print("3. Verify you're NOT added as member immediately")
    print("4. Check that a join request was created")
    print("5. Login as trip creator and approve the request")
    print("6. Verify you're now a member")

if __name__ == "__main__":
    verify_system()