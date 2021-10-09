git clone 'https://github.com/Mr-Destructive/emns_sqlite'
cd emns_sqlite

pip install virtualenv
virtualenv env
call env\Scripts\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
