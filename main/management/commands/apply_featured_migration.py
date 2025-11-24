from django.core.management.base import BaseCommand
from django.db import connection

class Command(BaseCommand):
    help = 'Manually add is_featured column if missing (for Render deployment)'

    def handle(self, *args, **options):
        try:
            with connection.cursor() as cursor:
                # Check if column exists
                cursor.execute("""
                    SELECT column_name 
                    FROM information_schema.columns 
                    WHERE table_name='main_trip' AND column_name='is_featured';
                """)
                
                if cursor.fetchone() is None:
                    self.stdout.write(self.style.WARNING('Column is_featured does not exist. Adding it...'))
                    
                    # Add the column
                    cursor.execute("""
                        ALTER TABLE main_trip 
                        ADD COLUMN is_featured BOOLEAN DEFAULT FALSE NOT NULL;
                    """)
                    
                    self.stdout.write(self.style.SUCCESS('✅ Successfully added is_featured column!'))
                else:
                    self.stdout.write(self.style.SUCCESS('✅ Column is_featured already exists!'))
                    
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'❌ Error: {str(e)}'))
            self.stdout.write(self.style.WARNING('Try running: python manage.py migrate'))
