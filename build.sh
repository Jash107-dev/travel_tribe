#!/usr/bin/env bash
# exit on error
set -o errexit

echo "🔧 Installing dependencies..."
pip install -r requirements.txt

echo "📦 Collecting static files..."
python manage.py collectstatic --no-input --verbosity 2

echo "🗄️  Running database migrations..."
python manage.py migrate --no-input --verbosity 2

echo "👤 Creating default user if needed..."
python create_default_user.py

echo "✅ Build complete!"
