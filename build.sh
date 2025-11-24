#!/usr/bin/env bash
# exit on error
set -o errexit
set -x  # Print commands as they execute

echo "🔧 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "📦 Collecting static files..."
python manage.py collectstatic --no-input --verbosity 2

echo "🗄️  Running database migrations..."
python manage.py migrate --no-input --verbosity 2

echo "🔧 Ensuring is_featured column exists..."
python manage.py apply_featured_migration || {
    echo "⚠️  Featured migration check failed (might not be needed)"
}

echo "👤 Creating default superuser if needed..."
python manage.py create_default_superuser || {
    echo "⚠️  Superuser creation failed (might already exist)"
}

echo "✅ Build complete!"