"""
WSGI config for travel_tribe project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
import sys
from pathlib import Path

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')

# Run migrations on first startup
BASE_DIR = Path(__file__).resolve().parent.parent
migration_flag = BASE_DIR / '.migrations_done'

if not migration_flag.exists():
    print("🔄 First startup detected - running migrations...")
    try:
        # Run the migration script
        import subprocess
        result = subprocess.run(
            [sys.executable, str(BASE_DIR / 'run_migrations_once.py')],
            capture_output=True,
            text=True
        )
        print(result.stdout)
        if result.returncode == 0:
            migration_flag.touch()
            print("✅ Migrations completed and flagged")
        else:
            print(f"❌ Migration failed: {result.stderr}")
    except Exception as e:
        print(f"⚠️  Migration error: {e}")

application = get_wsgi_application()
