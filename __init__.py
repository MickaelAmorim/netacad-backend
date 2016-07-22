from flask import Flask
from celery import Celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://cisco:cisco@localhost:5672/vhost'
app.config['CELERY_RESULT_BACKEND'] = 'amqp://cisco:cisco@localhost:5672/vhost'

celery = Celery(app.name, backend='amqp', broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)

import public
import csvProcess
