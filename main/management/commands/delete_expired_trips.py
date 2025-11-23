from django.core.management.base import BaseCommand
from django.utils import timezone
from datetime import date, timedelta
from main.models import Trip, TripPost

class Command(BaseCommand):
    help = 'Delete trips that have ended more than 7 days ago'

    def handle(self, *args, **options):
        # Delete trips that ended more than 7 days ago
        cutoff_date = date.today() - timedelta(days=7)
        
        # Delete expired destination trips
        expired_trips = Trip.objects.filter(end_date__lt=cutoff_date)
        trip_count = expired_trips.count()
        expired_trips.delete()
        
        # Delete expired trip posts (looking for tribe)
        expired_posts = TripPost.objects.filter(end_date__lt=cutoff_date)
        post_count = expired_posts.count()
        expired_posts.delete()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully deleted {trip_count} expired trips and {post_count} expired trip posts'
            )
        )