from celery import Celery
from time import sleep
from random import uniform
import mongoengine as mongo


mongo.connect(host='mongodb://localhost/celery_tutorial')


class Reversal(mongo.Document):
    """Represents a string and it's reversed version."""
    original = mongo.StringField(required=True)
    reversed = mongo.StringField(required=True)


# Instantiate, using RabbitMQ
app = Celery('tasks', broker='amqp://localhost//')


@app.task
def reverse(string):
    r = Reversal()
    r.original = string
    sleep(uniform(1, 4))
    reversed = string[::-1]
    r.reversed = reversed
    r.save()
    return 'saved: {} => {}'.format(string, reversed)
