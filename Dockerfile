FROM python:3.12-slim-bookworm

# Don't create .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
# Enable unbuffered output (helpful for logging)
ENV PYTHONUNBUFFERED=1

WORKDIR /code

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip --no-cache-dir
COPY requirements.txt .
RUN pip install -r requirements.txt --no-cache-dir
COPY . /code/
RUN python manage.py collectstatic --noinput || echo "Skipping collectstatic in dev"
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
