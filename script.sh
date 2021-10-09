#!/usr/bin/env bash

git clone 'https://github.com/Mr-Destructive/emns_sqlite'
cd emns_sqlite

pip install virtualenv
virtualenv env
source env/Script/activate

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

deactivate
