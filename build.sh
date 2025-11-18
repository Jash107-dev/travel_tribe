#!/usr/bin/env bash
# exit on error
set -o errexit
set -x  # Print commands as they execute

echo "🔧 Installing dependencies..."
pip install -r requirements.txt

echo "📦 Collecting static files..."
python manage.py collectstatic --no-input --verbosity 2

echo "🗄️  Running database migrations..."
echo "DATABASE_URL is set: ${DATABASE_URL:0:30}..."
python manage.py migrate --no-input --verbosity 2 || {
    echo "❌ Migration failed!"
    exit 1
}

echo "👤 Creating default user if needed..."
python create_default_user.py || {
    echo "⚠️  User creation failed (might already exist)"
}

echo "✅ Build complete!"
