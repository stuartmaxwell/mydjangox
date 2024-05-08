#!/bin/sh

if [ "$DB" = "postgresql" ]
then
    echo "Waiting for postgresql..."

    while ! nc -z $DB_HOST $DB_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

python manage.py migrate --no-input
python manage.py collectstatic --no-input

exec "$@"
