# A Flask App that Uses Celery

This is an expanded example based on video2's Flask app. It requires Celery, MongoDB, RabbitMQ, SQLite3, Flask, and Python 3.

Start Celery, pointing to the file and object (`app.celery`):

```
$ celery -A app.celery worker --loglevel=info
```

You should see a task available in the terminal:

```text
[tasks]
  . celery_example.insert
```

Start Mongo.

```
$ mongod
```

Make sure RabbitMQ is running.

Start the Flask app:

```
$ python app.py
```

To create the sqlite tables, visit http://localhost:5000/create-db just once.

There are routes to add the table data both synchronously (halting the browser) and asynchronously (browser sends reponse while sending the DB task off to RabbitMQ).
