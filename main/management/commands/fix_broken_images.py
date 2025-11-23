import os
from django.core.management.base import BaseCommand
from django.conf import settings
from main.models import Trip, TripImage, TripPhoto, UserProfile

class Command(BaseCommand):
    help = 'Check and fix broken image references'

    def handle(self, *args, **options):
        fixed_count = 0
        
        # Check Trip main images
        for trip in Trip.objects.exclude(main_image=''):
            if trip.main_image and not os.path.exists(trip.main_image.path):
                self.stdout.write(f"Broken main image for trip: {trip.destination}")
                trip.main_image = None
                trip.save()
                fixed_count += 1
        
        # Check TripImage gallery images
        for trip_image in TripImage.objects.all():
            if trip_image.image and not os.path.exists(trip_image.image.path):
                self.stdout.write(f"Broken gallery image for trip: {trip_image.trip.destination}")
                trip_image.delete()
                fixed_count += 1
        
        # Check TripPhoto images
        for trip_photo in TripPhoto.objects.all():
            if trip_photo.photo and not os.path.exists(trip_photo.photo.path):
                self.stdout.write(f"Broken photo for trip: {trip_photo.trip.destination}")
                trip_photo.delete()
                fixed_count += 1
        
        # Check UserProfile images
        for profile in UserProfile.objects.exclude(profile_picture=''):
            if profile.profile_picture and not os.path.exists(profile.profile_picture.path):
                self.stdout.write(f"Broken profile picture for user: {profile.user.username}")
                profile.profile_picture = None
                profile.save()
                fixed_count += 1
        
        self.stdout.write(
            self.style.SUCCESS(f'Fixed {fixed_count} broken image references')
        )