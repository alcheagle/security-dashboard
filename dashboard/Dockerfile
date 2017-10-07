FROM python:3.5-jessie

RUN pip install django
ADD . /usr/app/dashboard

WORKDIR /usr/app/dashboard

EXPOSE 8080

RUN python manage.py migrate

ENTRYPOINT python manage.py makemigrations && python manage.py runserver 0.0.0.0:8080
# ENTRYPOINT /bin/bash
