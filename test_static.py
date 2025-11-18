#!/usr/bin/env python
"""Test script to verify static files configuration"""
import os
import sys
from pathlib import Path

# Add project to path
BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travel_tribe.settings')
import django
django.setup()

from django.conf import settings
from django.contrib.staticfiles.finders import get_finders

print("=" * 60)
print("STATIC FILES CONFIGURATION TEST")
print("=" * 60)

print(f"\n✓ STATIC_URL: {settings.STATIC_URL}")
print(f"✓ STATIC_ROOT: {settings.STATIC_ROOT}")
print(f"✓ BASE_DIR: {settings.BASE_DIR}")

print("\n" + "=" * 60)
print("FINDING STATIC FILES...")
print("=" * 60)

found_files = []
for finder in get_finders():
    for path, storage in finder.list(None):
        if path.endswith('.css'):
            found_files.append(path)
            print(f"✓ Found: {path}")

print(f"\n{'=' * 60}")
print(f"TOTAL CSS FILES FOUND: {len(found_files)}")
print("=" * 60)

if len(found_files) > 0:
    print("\n✅ SUCCESS! Static files are configured correctly!")
else:
    print("\n❌ ERROR! No static files found!")
    sys.exit(1)
