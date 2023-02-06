../containers/wait-for-it.sh -t 60 db:5432
python manage.py migrate --noinput
python manage.py collectstatic --noinput
uwsgi --http :$VIRTUAL_PORT --module mysite.wsgi --static-map /static=/static --static-map /media=/media --processes 4 --threads 2
