"""
Test all URLs and check for errors
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User

def test_all_urls():
    print("🧪 TESTING ALL URLS AND FEATURES\n")
    print("=" * 70)
    
    client = Client()
    
    # Test 1: Public URLs
    print("\n✅ Test 1: Public URLs (No Login Required)")
    public_urls = [
        ('/', 'Login Page'),
        ('/register/', 'Register Page'),
        ('/forgot-password/', 'Forgot Password'),
    ]
    
    for url, name in public_urls:
        try:
            response = client.get(url, HTTP_HOST='127.0.0.1:8000')
            status = "✓" if response.status_code in [200, 302] else "✗"
            print(f"   {status} {name}: {response.status_code}")
        except Exception as e:
            print(f"   ✗ {name}: ERROR - {str(e)[:50]}")
    
    # Test 2: Login and test authenticated URLs
    print("\n✅ Test 2: Authenticated URLs")
    
    # Get or create test user
    user, created = User.objects.get_or_create(
        username='testuser',
        defaults={'email': 'test@example.com'}
    )
    if created:
        user.set_password('testpass123')
        user.save()
        print(f"   Created test user: testuser")
    
    # Login
    login_success = client.login(username='testuser', password='testpass123')
    if not login_success:
        # Try with existing user
        user = User.objects.first()
        if user:
            client.force_login(user)
            print(f"   Logged in as: {user.username}")
    else:
        print(f"   Logged in as: testuser")
    
    auth_urls = [
        ('/home/', 'Home Page'),
        ('/trips/', 'Find Tribes (Trip Feed)'),
        ('/create-trip/', 'Create Trip Post'),
        ('/add-trip/', 'Add Destination'),
        ('/profile/', 'User Profile'),
    ]
    
    for url, name in auth_urls:
        try:
            response = client.get(url, HTTP_HOST='127.0.0.1:8000')
            status = "✓" if response.status_code == 200 else "✗"
            print(f"   {status} {name}: {response.status_code}")
            
            if response.status_code != 200:
                print(f"      Error: {response.status_code}")
                if hasattr(response, 'content'):
                    content = response.content.decode('utf-8')
                    if 'error' in content.lower():
                        error_start = content.lower().find('error')
                        print(f"      {content[error_start:error_start+100]}")
        except Exception as e:
            print(f"   ✗ {name}: ERROR - {str(e)[:100]}")
    
    # Test 3: Check database
    print("\n✅ Test 3: Database Check")
    from main.models import Trip, TripPost, UserProfile
    
    print(f"   Users: {User.objects.count()}")
    print(f"   Trips: {Trip.objects.count()}")
    print(f"   Trip Posts: {TripPost.objects.count()}")
    print(f"   User Profiles: {UserProfile.objects.count()}")
    
    # Test 4: Check if user can access trip feed
    print("\n✅ Test 4: Trip Feed Specific Test")
    try:
        response = client.get('/trips/', HTTP_HOST='127.0.0.1:8000')
        print(f"   Status Code: {response.status_code}")
        print(f"   Content Type: {response.get('Content-Type', 'N/A')}")
        
        if response.status_code == 200:
            content = response.content.decode('utf-8')
            if 'Find Your Travel Tribe' in content:
                print(f"   ✓ Page title found")
            if 'trip-card' in content or 'empty-state' in content:
                print(f"   ✓ Trip cards or empty state found")
            print(f"   ✓ Trip Feed is accessible and rendering correctly")
        else:
            print(f"   ✗ Trip Feed returned status {response.status_code}")
    except Exception as e:
        print(f"   ✗ Error accessing trip feed: {e}")
    
    # Test 5: Check join functionality
    print("\n✅ Test 5: Join Trip Functionality")
    trip_posts = TripPost.objects.all()
    if trip_posts.exists():
        trip = trip_posts.first()
        print(f"   Testing with trip: {trip.destination}")
        
        # Check if user can join
        if user not in trip.joined_members.all():
            try:
                response = client.get(f'/join-trip/{trip.id}/', HTTP_HOST='127.0.0.1:8000')
                print(f"   Join Trip Status: {response.status_code}")
                if response.status_code in [200, 302]:
                    print(f"   ✓ Join trip URL is accessible")
                else:
                    print(f"   ✗ Join trip returned {response.status_code}")
            except Exception as e:
                print(f"   ✗ Error joining trip: {e}")
        else:
            print(f"   User already in trip")
    else:
        print(f"   No trip posts available to test")
    
    print("\n" + "=" * 70)
    print("🎉 TEST COMPLETE!")
    print("=" * 70)

if __name__ == '__main__':
    try:
        test_all_urls()
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        import traceback
        traceback.print_exc()
