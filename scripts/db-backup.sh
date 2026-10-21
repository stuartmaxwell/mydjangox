#!/usr/bin/env bash

# Run using cron to backup db every hour
# Ensure the following environment variables are set:
#  - DB_NAME
#  - AWS_ACCESS_KEY_ID
#  - AWS_SECRET_ACCESS_KEY
#  - BACKUPS_S3_ENDPOINT
#  - BACKUPS_S3_BUCKET

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
if [ "${HOUR}" == "00" ] && [ "${DAY}" == "01" ]; then
    echo "Performing a monthly backup."  # Each month is overwritten in a year's time
    SUFFIX="${HOUR}-${DAY}-${MONTH}"
elif [ "${HOUR}" == "00" ]; then
    echo "Performing a daily backup."  # Each day is overwritten in a month's time
    SUFFIX="${HOUR}-${DAY}"
else
    echo "Performing an hourly backup."  # Each hour is overwritten in a day's time
    SUFFIX="${HOUR}"
fi

DESTINATION="s3://${BACKUPS_S3_BUCKET}/backup-${DB_NAME}-${SUFFIX}.tar.gz"
echo "Uploading ${TAR_FILE} to S3: ${DESTINATION}"
s5cmd --endpoint-url "${BACKUPS_S3_ENDPOINT}" cp "${TAR_FILE}" "${DESTINATION}"

echo "Backup complete."
