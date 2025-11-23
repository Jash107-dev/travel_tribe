from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Reset admin user with correct permissions'

    def handle(self, *args, **options):
        # Delete existing admin user if exists
        try:
            existing_user = User.objects.get(username='Jashwanth')
            existing_user.delete()
            self.stdout.write('🗑️ Deleted existing admin user')
        except User.DoesNotExist:
            pass
        
        # Create fresh admin user
        admin_user = User.objects.create_superuser(
            username='Jashwanth',
            email='jashwanth@traveltribe.com',
            password='Jash@2289'
        )
        
        # Ensure all permissions are set
        admin_user.is_superuser = True
        admin_user.is_staff = True
        admin_user.is_active = True
        admin_user.save()
        
        self.stdout.write(
            self.style.SUCCESS(
                f'✅ Admin user "{admin_user.username}" created successfully!'
            )
        )
        self.stdout.write(f'   - Username: {admin_user.username}')
        self.stdout.write(f'   - Email: {admin_user.email}')
        self.stdout.write(f'   - Is superuser: {admin_user.is_superuser}')
        self.stdout.write(f'   - Is staff: {admin_user.is_staff}')
        self.stdout.write(f'   - Is active: {admin_user.is_active}')