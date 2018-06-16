# A Flask App that Uses Celery

Start Celery:

```
$ celery -A celery_example.celery worker --loglevel=info
```

Start Mongo.

```
$ mongod
```

Start the Flask app:

```
$ python celery_example.py
```

Then visit a URL like http://localhost:5000/process/some-string
