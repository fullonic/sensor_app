#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z sensors-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

echo "STARTING APP"
python manage.py run -h 0.0.0.0  && curl http://localhost:5001/main/real_time
# gunicorn 0.0.0.0:5000 manage:app
