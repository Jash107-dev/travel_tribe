from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import os

class Command(BaseCommand):
    help = 'Create default superuser if none exists'

    def handle(self, *args, **options):
        # SECURITY: Only create ONE admin EVER
        existing_admins = User.objects.filter(is_superuser=True)
        
        if not existing_admins.exists():
            # Create the ONLY superuser
            username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
            email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@traveltribe.com')
            password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin123')
            
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            
            self.stdout.write(
                self.style.SUCCESS(
                    f'✅ ONLY Superuser "{username}" created successfully!'
                )
            )
            self.stdout.write(
                self.style.WARNING(
                    f'🔐 Login at: /admin/ with username: {username}'
                )
            )
            self.stdout.write(
                self.style.ERROR(
                    '🔒 SECURITY: Admin creation is now PERMANENTLY DISABLED'
                )
            )
        else:
            admin_count = existing_admins.count()
            self.stdout.write(
                self.style.SUCCESS(f'✅ Superuser already exists ({admin_count} admin(s))')
            )
            self.stdout.write(
                self.style.ERROR(
                    '🔒 SECURITY: No additional admins can be created'
                )
            )