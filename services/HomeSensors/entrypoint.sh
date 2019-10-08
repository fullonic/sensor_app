#!/bin/sh

echo "Waiting for postgres..."

while ! nc -z sensors-db 5432; do
  sleep 0.1
done

echo "PostgreSQL started"

echo "STARTING APP"
gunicorn -b 0.0.0.0:5000 manage:app
