#!/usr/bin/env bash

# Run using cron to backup db every hour
# Ensure the following environment variables are set:
#  - AWS_ACCESS_KEY_ID
#  - AWS_SECRET_ACCESS_KEY
#  - AWS_ENDPOINT_URL
#  - S3_BUCKET

set -euf -o pipefail

DB_PATH="/app/db/${DB_NAME}.sqlite3"  # Path to the SQLite database
BACKUP_DIR="/app/db/backup"  # Directory to store backups
HOUR=$(date +%H)  # Current hour
DAY=$(date +%d)  # Current day
MONTH=$(date +%m)  # Current month
BACKUP_FILE="${BACKUP_DIR}/latestbackup.sqlite3"  # Temporary backup file
TAR_FILE="${BACKUP_DIR}/latestbackup.tar.gz"  # Compressed backup file

echo "Backing up SQLite database to ${TAR_FILE}..."

# Ensure the backup directory exists
echo "Ensuring backup directory exists..."
mkdir -p "${BACKUP_DIR}"

# Backup the SQLite database
echo "Backing up SQLite database..."
sqlite3 "${DB_PATH}" "VACUUM INTO '${BACKUP_FILE}'"

# Compress the backup
echo "Compressing backup..."
tar --gzip -cf "${TAR_FILE}" -C "${BACKUP_DIR}" "$(basename "${BACKUP_FILE}")"

# Remove the temporary backup file, but keep the compressed backup
echo "Remove backup file..."
rm "${BACKUP_FILE}"

# Upload to S3
echo "Hourly backup."  # Each hour is overwritten in a day's time
echo "Uploading ${TAR_FILE} to S3: s3://${S3_BUCKET}/backup-${DB_NAME}-${HOUR}.tar.gz"
s5cmd --endpoint-url ${AWS_ENDPOINT_URL} cp "${TAR_FILE}" "s3://${S3_BUCKET}/backup-${DB_NAME}-${HOUR}.tar.gz"

echo "Daily backup."  # Each day is overwritten in a month's time
if [ "${HOUR}" == "00" ]; then
    echo "Uploading ${TAR_FILE} to S3: s3://${S3_BUCKET}/backup-${DB_NAME}-${DAY}-${HOUR}.tar.gz"
    s5cmd --endpoint-url ${AWS_ENDPOINT_URL} cp "${TAR_FILE}" "s3://${S3_BUCKET}/backup-${DB_NAME}-${DAY}-${HOUR}.tar.gz"
fi

echo "Monthly backup."  # Each month is overwritten in a year's time
if [ "${HOUR}" == "00" ] && [ "${DAY}" == "01" ]; then
    echo "Uploading ${TAR_FILE} to S3: s3://${S3_BUCKET}/backup-${DB_NAME}-${MONTH}-${DAY}-${HOUR}.tar.gz"
    s5cmd --endpoint-url ${AWS_ENDPOINT_URL} cp "${TAR_FILE}" "s3://${S3_BUCKET}/backup-${DB_NAME}-${MONTH}-${DAY}-${HOUR}.tar.gz"
fi

echo "Backup complete."
