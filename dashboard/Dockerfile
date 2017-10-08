FROM python:3.4-jessie

RUN pip install Django
RUN pip install gunicorn
RUN pip install mongoengine
RUN pip install ipython #DEBUG ONLY
# COPY . /usr/app/dashboard

WORKDIR /usr/app/dashboard

EXPOSE 8080

ENTRYPOINT gunicorn dashboard.wsgi:application --bind 0.0.0.0:8080 --workers 4
