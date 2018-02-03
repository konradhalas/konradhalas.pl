FROM python:3.6.4

RUN pip install uwsgi==2.0.15

RUN pip install pipenv==9.0.3

ADD /Pipfile /app/Pipfile

ADD /Pipfile.lock /app/Pipfile.lock

WORKDIR /app/

RUN pipenv install --system

ADD / /app

WORKDIR /app/mysite

CMD ../containers/run.sh