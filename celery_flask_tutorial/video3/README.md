# Third Video

Start Celery:

```
$ celery -A tasks worker --loglevel=info
```

Start Mongo:

```
$ mongod
```

Start a Python REPL:

```
>>> from tasks import *
>>> process_data('some string')  # synchronous
>>> process_data.delay('some string')  # async
>>> result = process_data.delay('some string')
>>> result  # => 'PENDING'
>>> result  # => 'PENDING'
>>> result  # => 'PENDING'
>>> result  # => 'SUCCESS'
```

In the meantime, Mongo (or whatever backend is connected) will be recording. You can see sample data with `db.celery_taskmeta.findOne()`.

```json
{
        "_id" : "c62b82a6-0e28-425b-a9cb-4e0a0da0c341",
        "date_done" : ISODate("2018-06-16T15:01:59.866Z"),
        "children" : "[]",
        "traceback" : "null",
        "status" : "SUCCESS",
        "result" : "\"fdsa\""
}
```

And those fields will be available on the `result` variable in Python, mentioned above:

```
>>> result.id  # => 'c62b82a6-0e28-425b-a9cb-4e0a0da0c341'
>>> result.result  # => 'fdsa'
```

There are other methods available:

```python
result.ready()  # Boolean
result.get()    # Show the result
```
