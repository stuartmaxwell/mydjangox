#!/bin/bash

# Exit immediately if any command fails
set -euf -o pipefail

BACKUP_PATH="/app/db"  # This must match the path in the Dockerfile and backup.sh
DB_PATH="${BACKUP_PATH}/${DB_NAME}.sqlite3"
TEMP_RESTORE_FILE="${BACKUP_PATH}/latest-backup.tar.gz"

# Function to download the latest SQLite database backup from S3
download_latest_backup() {
    echo "Downloading latest SQLite database backup from S3..."
    # This will give us the file name of the most recent backup.
    # s5cmd ls doesn't have a direct sort option, so we'll pipe to sort
    LATEST_BACKUP=$(s5cmd --endpoint-url "${AWS_ENDPOINT_URL}" ls "s3://${S3_BUCKET}/**" | sort | tail -n 1 | awk '{print $NF}')

    if [ -z "${LATEST_BACKUP}" ]; then
        # There's no backup so nothing to do.
        echo "No backup found in S3 bucket."
    else
        # Found a backup, download and extract it
        echo "Latest backup found: ${LATEST_BACKUP}"
        s5cmd --endpoint-url "${AWS_ENDPOINT_URL}" cp s3://${S3_BUCKET}/${LATEST_BACKUP} "${TEMP_RESTORE_FILE}"
        tar --gzip -xf "${TEMP_RESTORE_FILE}" -O > "${DB_PATH}"
        # Clean up the temporary file we downloaded
        rm "${TEMP_RESTORE_FILE}"
        echo "SQLite database backup downloaded and extracted."
    fi
}

# Check if the database file exists - if it doesn't, download the latest backup
echo "Checking if SQLite database file exists"
if [ ! -f "${DB_PATH}" ]; then
    download_latest_backup
fi

# Apply database migrations
echo "Applying database migrations"
uv run --no-cache manage.py migrate --noinput

# Collect static files
echo "Collecting static files"
uv run --no-cache manage.py collectstatic --noinput

# Start the Django server with Gunicorn
echo "Starting server"
exec "$@"
