FROM python:3.12-slim-bookworm

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y build-essential curl libpq-dev --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE 1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED 1

# Install pip requirements
RUN python -m pip install --upgrade pip
COPY requirements.txt /app/requirements.txt
RUN python -m pip install -r /app/requirements.txt

WORKDIR /app
COPY . /app
RUN mkdir /app/staticfiles

# Switching to a non-root user
RUN useradd appuser && chown -R appuser /app
USER appuser

# Expose port 8000 for Gunicorn
EXPOSE 8000
