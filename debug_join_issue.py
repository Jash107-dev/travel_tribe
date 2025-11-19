#!/usr/bin/env python
"""
Debug why users are still joining directly
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import Trip, JoinRequest

def debug_join_issue():
    print("🔍 DEBUGGING JOIN ISSUE")
    print("=" * 40)
    
    # Check all trips and their members
    trips = Trip.objects.all()
    
    for trip in trips:
        print(f"\n🎯 Trip: {trip.destination}")
        print(f"   Creator: {trip.created_by.username}")
        print(f"   Members: {trip.members_count}/{trip.members_limit}")
        
        # List all members
        members = trip.joined_members.all()
        if members:
            print("   👥 Current members:")
            for member in members:
                print(f"      - {member.username}")
                
                # Check if this member has an approved request
                try:
                    request = JoinRequest.objects.get(trip=trip, user=member, status='approved')
                    print(f"        ✅ Has approved request")
                except JoinRequest.DoesNotExist:
                    print(f"        ❌ NO REQUEST FOUND - JOINED DIRECTLY!")
        
        # List all requests
        requests = JoinRequest.objects.filter(trip=trip)
        if requests:
            print("   📋 Join requests:")
            for req in requests:
                print(f"      - {req.user.username}: {req.status}")
        else:
            print("   📋 No join requests")
    
    print(f"\n📊 SUMMARY:")
    print(f"   Total trips: {trips.count()}")
    print(f"   Total requests: {JoinRequest.objects.count()}")
    
    # Check for members without requests
    problem_members = []
    for trip in trips:
        for member in trip.joined_members.all():
            if member != trip.created_by:  # Skip trip creator
                try:
                    JoinRequest.objects.get(trip=trip, user=member, status='approved')
                except JoinRequest.DoesNotExist:
                    problem_members.append((member.username, trip.destination))
    
    if problem_members:
        print(f"\n❌ PROBLEM FOUND:")
        print(f"   {len(problem_members)} members joined without approved requests:")
        for username, destination in problem_members:
            print(f"      - {username} in {destination}")
    else:
        print(f"\n✅ NO PROBLEMS FOUND - All members have approved requests")

if __name__ == "__main__":
    debug_join_issue()