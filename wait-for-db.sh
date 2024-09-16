#!/bin/sh

# Espera a que el servicio de base de datos esté disponible
echo "Waiting for MySQL..."

while ! nc -z db 3306; do
  sleep 1
done

echo "MySQL is up - executing command"

exec "$@"
