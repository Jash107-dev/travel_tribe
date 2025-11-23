#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🔧 Installing dependencies..."
pip install --upgrade pip --no-cache-dir
pip install -r requirements.txt --no-cache-dir

echo "📦 Collecting static files..."
python manage.py collectstatic --no-input --clear

echo "🗄️  Running database migrations..."
python manage.py migrate --no-input

echo "👤 Creating default superuser if needed..."
python manage.py create_default_superuser || echo "⚠️  Superuser already exists"

echo "✅ Build complete!"