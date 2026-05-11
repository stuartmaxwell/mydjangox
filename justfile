# Set the default recipe to list all available commands
default:
    @just --list

# Create and/or update the lockfile with the latest packages. Note that the "--exclude-newer 7d" option will be added when released.
lock:
  pdm lock --exclude-newer 7d

# Install/sync packages in the virtual environment
sync:
  pdm sync --clean

# Run the Django development server
run:
    pdm run manage.py runserver

# Make migrations
makemigrations:
    pdm run manage.py makemigrations

# Apply migrations
migrate:
    pdm run manage.py migrate

# Create a superuser
createsuperuser:
    pdm run manage.py createsuperuser

# Collect static files
collectstatic:
    pdm run manage.py collectstatic

# Run Django shell
shell:
    pdm run manage.py shell

# Check for any problems in your project
check:
    pdm run manage.py check

# Generate a secret key for Django
secret:
  pdm run manage.py shell -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"

# Create a new Django app
startapp APPNAME:
    pdm run manage.py startapp {{APPNAME}}

# Generic manage command
manage ARGS="":
    pdm run manage.py {{ARGS}}

# Run pytest
test:
    pdm run pytest

# Install pre-commit hooks
pc-install:
    pre-commit install

# Upgrade pre-commit hooks
pc-up:
    pre-commit autoupdate

# Run pre-commit hooks
pc-run:
    pre-commit run --all-files

# Run Docker compose up on the development environment
dc-up-dev:
    docker compose --file docker-compose-dev.yml up -d --build

# Run Docker compose logs on the development environment
dc-logs-dev:
    docker compose --file docker-compose-dev.yml logs -f

# Run a terminal on the development environment
dc-exec-dev:
    docker compose --file docker-compose-dev.yml exec app /bin/bash
