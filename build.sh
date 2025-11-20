#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🔧 Installing dependencies..."
pip install -r requirements.txt

echo "📦 Collecting static files..."
python manage.py collectstatic --no-input

echo "🗄️  Running database migrations..."
python manage.py migrate --no-input

echo "👤 Creating default superuser if needed..."
python manage.py create_default_superuser || echo "⚠️  Superuser creation failed (might already exist)"

echo "✅ Build complete!"