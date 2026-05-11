#!/bin/bash

# Exit immediately if any command fails
set -euf -o pipefail

# Check and restore database
echo "Checking and restoring database"
scripts/db-restore.sh

# Apply database migrations
echo "Applying database migrations"
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files"
python manage.py collectstatic --noinput

# Start the Django server with Gunicorn
echo "Starting server"
exec gunicorn --worker-tmp-dir /dev/shm --workers=2 --max-requests=1000 --max-requests-jitter=50 --bind 0.0.0.0:8000 config.wsgi:application
