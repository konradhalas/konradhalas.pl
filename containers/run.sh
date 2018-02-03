../containers/wait-for-it.sh -t 60 db:5432
python manage.py migrate --noinput
python manage.py collectstatic --noinput
uwsgi --http :8000 --module mysite.wsgi --processes 4 --threads 2