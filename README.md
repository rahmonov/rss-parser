# Lenta.ru rss parser

It is a digest website from the website http://lenta.ru

## In backend

The app gets news from the rss of lenta.ru and saves in the database every minute

## In frontend

User can filter through the news and send a pdf report to an email

## Tech stack

 - Django
 - DRF
 - SQLite
 - Celery
 - RabbitMQ
 - AngularJS + Angular Material
 
## Installation

Simply do `pip install -r requirements.txt` after cloning

Then start RabbitMQ by `sudo rabbitmq-server start`

Then start Celery by `celery -A trial worker -l info`

Then start Celery beat by `celery -A trial beat`

### P.S. the project name need to be changed from `trial` to something more appropriate
