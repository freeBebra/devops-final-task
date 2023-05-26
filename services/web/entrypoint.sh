#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if [ $# = 1 ]; then
    if [ $1 = "test" ]; then
      python -m unittest tests.py
    fi
fi

python manage.py create_db

exec "$@"
