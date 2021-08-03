#!/bin/sh
cd app
rm -d -r migrations/
cd ..
rm -d -r db.sqlite3
python manage.py makemigrations app
python manage.py migrate
python manage.py createsuperuser