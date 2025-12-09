from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Fix UserProfile table by removing old gamification columns'

    def handle(self, *args, **options):
        if connection.vendor != 'postgresql':
            self.stdout.write(self.style.WARNING('This command only works with PostgreSQL'))
            return
        
        with connection.cursor() as cursor:
            try:
                # Drop badges column
                self.stdout.write('Checking badges column...')
                cursor.execute("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name='main_userprofile' AND column_name='badges';
                """)
                if cursor.fetchone():
                    self.stdout.write('Dropping badges column...')
                    cursor.execute('ALTER TABLE main_userprofile DROP COLUMN badges;')
                    self.stdout.write(self.style.SUCCESS('✓ Dropped badges column'))
                else:
                    self.stdout.write(self.style.SUCCESS('✓ badges column already removed'))
                
                # Drop level column
                self.stdout.write('Checking level column...')
                cursor.execute("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name='main_userprofile' AND column_name='level';
                """)
                if cursor.fetchone():
                    self.stdout.write('Dropping level column...')
                    cursor.execute('ALTER TABLE main_userprofile DROP COLUMN level;')
                    self.stdout.write(self.style.SUCCESS('✓ Dropped level column'))
                else:
                    self.stdout.write(self.style.SUCCESS('✓ level column already removed'))
                
                # Drop points column
                self.stdout.write('Checking points column...')
                cursor.execute("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name='main_userprofile' AND column_name='points';
                """)
                if cursor.fetchone():
                    self.stdout.write('Dropping points column...')
                    cursor.execute('ALTER TABLE main_userprofile DROP COLUMN points;')
                    self.stdout.write(self.style.SUCCESS('✓ Dropped points column'))
                else:
                    self.stdout.write(self.style.SUCCESS('✓ points column already removed'))
                
                self.stdout.write(self.style.SUCCESS('\n✅ UserProfile table fixed successfully!'))
                self.stdout.write(self.style.SUCCESS('Registration should now work properly.'))
                
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'❌ Error: {str(e)}'))
