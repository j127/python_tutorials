# Python, Flask, Celery, RabbitMQ Tutorial

Learning a bit of RabbitMQ via [this playlist](https://www.youtube.com/playlist?list=PLXmMXHVSvS-DvYrjHcZOg7262I9sGBLFR).

## Running It

Install Celery, RabbitMQ, and MongoDB.

Install the Python requirements into a Python3 virtual environment:

```
$ pip install -r requirements.txt
```

Start Celery:

```
$ celery -A tasks worker --loglevel=info
```

Open a Python REPL and use it:

```
>>> from tasks import reverse
>>> reverse.delay('some string')
```

Each reverse will have a delay before appearing in MongoDB.
