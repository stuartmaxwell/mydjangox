FROM python:3.13-slim-bookworm

# Install system dependencies
RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y sqlite3 curl --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean

# install s5cmd
COPY --from=peakcom/s5cmd:latest /s5cmd /usr/local/bin/s5cmd

# install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /usr/local/bin/uv

# - Silence uv complaining about not being able to use hard links,
# - tell uv to byte-compile packages for faster application startups,
# - prevent uv from accidentally downloading isolated Python builds,
# - pick a Python,
ENV UV_LINK_MODE=copy \
  UV_COMPILE_BYTECODE=1 \
  UV_PYTHON_DOWNLOADS=never \
  UV_PYTHON=python3.13

# Create directory for the datatbase
RUN mkdir -p /app/db

# Add the backup script
COPY backup.sh /app/

# Add the entrypoint script
COPY entrypoint.sh /app/

# Set up the environment
COPY pyproject.toml /app/
COPY uv.lock /app/
WORKDIR /app
RUN uv sync --locked --no-dev

# Copy the rest of the application
COPY . /app
RUN mkdir /app/staticfiles

RUN chmod +x /app/backup.sh
RUN chmod +x /app/entrypoint.sh

# Switching to a non-root user
RUN useradd appuser && chown -R appuser /app
USER appuser

# Expose the port
EXPOSE 8000
