ARG PYTHON_BASE=3.14-slim

# --- BUILD STAGE ---
FROM python:$PYTHON_BASE AS builder
ENV PDM_CHECK_UPDATE=false

# install s5cmd
COPY --from=peakcom/s5cmd:latest /s5cmd /usr/local/bin/s5cmd

# Build Python Environment
RUN pip install -U pdm
WORKDIR /app
COPY pyproject.toml pdm.lock ./
RUN pdm install --check --prod --no-editable


# --- RUN STAGE ---
FROM python:$PYTHON_BASE
WORKDIR /app

# Standard Python production settings
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# Install system dependencies
RUN apt-get update \
  && apt-get install -y sqlite3 curl --no-install-recommends \
  && rm -rf /var/lib/apt/lists/* /usr/share/doc /usr/share/man \
  && apt-get clean

# Copy the static binaries
COPY --from=builder /usr/local/bin/s5cmd /usr/local/bin/s5cmd
COPY --from=builder /usr/bin/infisical /usr/bin/infisical

# Create the user first (This layer stays cached unless you change the name)
RUN useradd -m appuser

# Create the directories and set ownership in one go
RUN mkdir -p /app/staticfiles \
  && mkdir -p /app/db \
  && chown -R appuser:appuser /app/

# Copy the Virtual Env (Set ownership during the copy)
COPY --from=builder --chown=appuser:appuser /app/.venv/ /app/.venv
ENV PATH="/app/.venv/bin:$PATH"

# Copy the application code (Set ownership during the copy)
COPY --chown=appuser:appuser . .

# Fix permissions
RUN chmod +x /app/backup.sh \
  && chmod +x /app/entrypoint.sh

USER appuser
EXPOSE 8000
ENTRYPOINT ["/app/entrypoint.sh"]
