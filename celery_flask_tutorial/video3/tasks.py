from time import sleep
from random import uniform
from celery import Celery

# See the code in video2 for something that appears to have the same
# result as `backend` here.
app = Celery(
    'tasks',
    broker='amqp://localhost//',
    backend='mongodb://localhost/celery_video3'
)


@app.task
def process_data(data):
    """Do some long-running task here."""
    sleep(uniform(1, 5))
    return data[::-1]


