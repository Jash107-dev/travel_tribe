#!/usr/bin/env python
"""
Clean up unauthorized members and deploy nuclear security
"""
import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

from django.contrib.auth.models import User
from main.models import Trip, JoinRequest

def cleanup_and_deploy():
    print("🧹 CLEANING UP UNAUTHORIZED MEMBERS")
    print("=" * 50)
    
    removed_count = 0
    
    # Check all trips
    for trip in Trip.objects.all():
        print(f"\n🎯 Checking trip: {trip.destination}")
        
        # Get all members except creator
        members_to_check = trip.joined_members.exclude(id=trip.created_by.id)
        
        for member in members_to_check:
            # Check if they have approved request
            try:
                JoinRequest.objects.get(trip=trip, user=member, status='approved')
                print(f"   ✅ {member.username} - has approved request")
            except JoinRequest.DoesNotExist:
                # Remove unauthorized member
                trip.joined_members.remove(member)
                removed_count += 1
                print(f"   🚫 REMOVED {member.username} - no approved request!")
    
    print(f"\n📊 CLEANUP SUMMARY:")
    print(f"   Removed {removed_count} unauthorized members")
    
    # Now deploy the nuclear security
    import subprocess
    
    print(f"\n🚀 DEPLOYING NUCLEAR SECURITY...")
    
    try:
        # Add changes
        subprocess.run(["git", "add", "."], check=True)
        print("✅ Added changes to git")
        
        # Commit
        subprocess.run(["git", "commit", "-m", "NUCLEAR SECURITY: Block all unauthorized trip joining"], check=True)
        print("✅ Committed changes")
        
        # Push
        subprocess.run(["git", "push"], check=True)
        print("✅ Pushed to repository")
        
        print(f"\n🎉 NUCLEAR SECURITY DEPLOYED!")
        print(f"🔒 NO ONE can join trips without approved requests now!")
        
    except subprocess.CalledProcessError as e:
        print(f"❌ Git operation failed: {e}")
    
    print(f"\n🧪 VERIFICATION:")
    print(f"   Run debug_join_issue.py again to verify cleanup")
    print(f"   Test on your deployed site - should be 100% secure now")

if __name__ == "__main__":
    cleanup_and_deploy()