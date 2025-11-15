"""
Management command to seed the database with sample travel data
Usage: python manage.py seed_data
"""

from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from main.models import Trip, TripPost, ChatRoom, ChatMessage
from datetime import datetime, timedelta
import random


class Command(BaseCommand):
    help = 'Seeds the database with sample trips and users'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('🌍 Starting database seeding...'))

        # Create admin user if doesn't exist
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@traveltribe.com',
                'is_staff': True,
                'is_superuser': True
            }
        )
        if created:
            admin_user.set_password('admin123')
            admin_user.save()
            self.stdout.write(self.style.SUCCESS('✅ Admin user created (username: admin, password: admin123)'))
        else:
            self.stdout.write(self.style.WARNING('⚠️  Admin user already exists'))

        # Create sample users
        sample_users = []
        user_data = [
            ('rahul_traveler', 'rahul@example.com'),
            ('priya_explorer', 'priya@example.com'),
            ('amit_wanderer', 'amit@example.com'),
            ('sneha_nomad', 'sneha@example.com'),
            ('vikram_adventurer', 'vikram@example.com'),
        ]

        for username, email in user_data:
            user, created = User.objects.get_or_create(
                username=username,
                defaults={'email': email}
            )
            if created:
                user.set_password('password123')
                user.save()
                self.stdout.write(self.style.SUCCESS(f'✅ Created user: {username}'))
            sample_users.append(user)

        # Sample trip data
        trips_data = [
            {
                'destination': 'Manali from Hyderabad',
                'category': 'Within Country',
                'description': 'Experience the snow-capped mountains, adventure sports, and serene valleys of Manali. Perfect for both adventure seekers and peace lovers.',
                'start_date': datetime.now().date() + timedelta(days=30),
                'end_date': datetime.now().date() + timedelta(days=37),
                'tribe_count': 6,
                'food_type': 'Both',
                'transport_modes': 'Flight to Chandigarh, then Cab to Manali',
                'must_visit_places': 'Rohtang Pass, Solang Valley, Old Manali, Hadimba Temple, Vashisht Hot Springs',
                'must_try_foods': 'Siddu, Thukpa, Momos, Trout Fish, Local Himachali Thali',
            },
            {
                'destination': 'Vizag from Hyderabad',
                'category': 'Within Country',
                'description': 'Explore the beautiful beaches, ancient caves, and scenic hills of Visakhapatnam. A perfect coastal getaway with rich history.',
                'start_date': datetime.now().date() + timedelta(days=15),
                'end_date': datetime.now().date() + timedelta(days=18),
                'tribe_count': 4,
                'food_type': 'Both',
                'transport_modes': 'Train or Bus (8-10 hours)',
                'must_visit_places': 'RK Beach, Borra Caves, Araku Valley, Kailasagiri, Submarine Museum',
                'must_try_foods': 'Bamboo Chicken, Pesarattu, Seafood Platter, Araku Coffee, Pootharekulu',
            },
            {
                'destination': 'Varanasi from Hyderabad',
                'category': 'Within Country',
                'description': 'Discover the spiritual heart of India. Experience ancient temples, Ganga Aarti, and the timeless culture of this holy city.',
                'start_date': datetime.now().date() + timedelta(days=45),
                'end_date': datetime.now().date() + timedelta(days=49),
                'tribe_count': 5,
                'food_type': 'Veg',
                'transport_modes': 'Flight or Train (Direct trains available)',
                'must_visit_places': 'Kashi Vishwanath Temple, Dashashwamedh Ghat, Sarnath, Assi Ghat, Manikarnika Ghat',
                'must_try_foods': 'Kachori Sabzi, Banarasi Paan, Lassi, Chaat, Malaiyo',
            },
            {
                'destination': 'Goa Beach Paradise',
                'category': 'Within Country',
                'description': 'Sun, sand, and sea! Enjoy the vibrant nightlife, Portuguese architecture, and pristine beaches of Goa.',
                'start_date': datetime.now().date() + timedelta(days=20),
                'end_date': datetime.now().date() + timedelta(days=25),
                'tribe_count': 8,
                'food_type': 'Both',
                'transport_modes': 'Flight to Goa Airport',
                'must_visit_places': 'Baga Beach, Fort Aguada, Dudhsagar Falls, Old Goa Churches, Anjuna Flea Market',
                'must_try_foods': 'Fish Curry Rice, Bebinca, Vindaloo, Xacuti, Feni',
            },
            {
                'destination': 'Ladakh Adventure',
                'category': 'Within Country',
                'description': 'The land of high passes! Experience breathtaking landscapes, Buddhist monasteries, and thrilling bike rides.',
                'start_date': datetime.now().date() + timedelta(days=60),
                'end_date': datetime.now().date() + timedelta(days=70),
                'tribe_count': 6,
                'food_type': 'Both',
                'transport_modes': 'Flight to Leh',
                'must_visit_places': 'Pangong Lake, Nubra Valley, Khardung La Pass, Leh Palace, Magnetic Hill',
                'must_try_foods': 'Thukpa, Momos, Butter Tea, Skyu, Tingmo',
            },
            {
                'destination': 'Dubai Luxury Escape',
                'category': 'Outside Country',
                'description': 'Experience luxury and modernity in the desert! Skyscrapers, shopping, and desert safaris await.',
                'start_date': datetime.now().date() + timedelta(days=90),
                'end_date': datetime.now().date() + timedelta(days=96),
                'tribe_count': 4,
                'food_type': 'Both',
                'transport_modes': 'Direct Flight from Hyderabad',
                'must_visit_places': 'Burj Khalifa, Dubai Mall, Palm Jumeirah, Desert Safari, Dubai Marina',
                'must_try_foods': 'Shawarma, Kunafa, Al Harees, Luqaimat, Arabic Coffee',
            },
        ]

        # Create trips
        created_trips = []
        for trip_data in trips_data:
            trip, created = Trip.objects.get_or_create(
                destination=trip_data['destination'],
                created_by=admin_user,
                defaults=trip_data
            )
            if created:
                self.stdout.write(self.style.SUCCESS(f'✅ Created trip: {trip.destination}'))
                created_trips.append(trip)
            else:
                self.stdout.write(self.style.WARNING(f'⚠️  Trip already exists: {trip.destination}'))

        # Create TripPosts (for tribe finder)
        trip_posts_data = [
            {
                'destination': 'Rishikesh Yoga Retreat',
                'interests': 'Relaxation',
                'gender_preference': 'Any',
                'budget_range': '₹8000 - ₹12000',
                'members_limit': 6,
                'description': 'Looking for peaceful souls to join a yoga and meditation retreat in Rishikesh. River rafting optional!',
                'start_date': datetime.now().date() + timedelta(days=25),
                'end_date': datetime.now().date() + timedelta(days=29),
            },
            {
                'destination': 'Jaipur Heritage Tour',
                'interests': 'Culture',
                'gender_preference': 'Any',
                'budget_range': '₹10000 - ₹15000',
                'members_limit': 5,
                'description': 'Explore the Pink City! Forts, palaces, and authentic Rajasthani cuisine. History buffs welcome!',
                'start_date': datetime.now().date() + timedelta(days=35),
                'end_date': datetime.now().date() + timedelta(days=39),
            },
            {
                'destination': 'Coorg Coffee Plantations',
                'interests': 'Relaxation',
                'gender_preference': 'Any',
                'budget_range': '₹6000 - ₹9000',
                'members_limit': 4,
                'description': 'Weekend getaway to the Scotland of India. Coffee estates, waterfalls, and misty hills.',
                'start_date': datetime.now().date() + timedelta(days=12),
                'end_date': datetime.now().date() + timedelta(days=15),
            },
            {
                'destination': 'Spiti Valley Expedition',
                'interests': 'Adventure',
                'gender_preference': 'Any',
                'budget_range': '₹20000 - ₹30000',
                'members_limit': 8,
                'description': 'Epic road trip through the Himalayas! High altitude lakes, ancient monasteries, and starry nights.',
                'start_date': datetime.now().date() + timedelta(days=75),
                'end_date': datetime.now().date() + timedelta(days=85),
            },
        ]

        for i, post_data in enumerate(trip_posts_data):
            user = sample_users[i % len(sample_users)]
            trip_post, created = TripPost.objects.get_or_create(
                destination=post_data['destination'],
                user=user,
                defaults=post_data
            )
            
            if created:
                # Add some random members
                num_members = random.randint(1, min(3, post_data['members_limit'] - 1))
                available_users = [u for u in sample_users if u != user]
                members_to_add = random.sample(available_users, num_members)
                trip_post.joined_members.add(*members_to_add)
                
                # Chatroom is auto-created by signal, no sample messages added
                
                self.stdout.write(self.style.SUCCESS(
                    f'✅ Created trip post: {trip_post.destination} with {num_members} members (empty chat)'
                ))

        self.stdout.write(self.style.SUCCESS('\n🎉 Database seeding completed successfully!'))
        self.stdout.write(self.style.SUCCESS('\n📝 Summary:'))
        self.stdout.write(f'   - Admin user: admin / admin123')
        self.stdout.write(f'   - Sample users: {len(sample_users)} (password: password123)')
        self.stdout.write(f'   - Destination trips: {len(trips_data)}')
        self.stdout.write(f'   - Active tribe posts: {len(trip_posts_data)}')
        self.stdout.write(self.style.SUCCESS('\n✨ You can now run: python manage.py runserver'))
