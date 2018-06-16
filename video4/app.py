from flask import Flask, request
from flask_celery import make_celery
from time import sleep
from random import uniform, choice
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'mongodb://localhost/'
app.config['CELERY_MONGODB_BACKEND_SETTINGS'] = {
    'database': 'celery_result_backend_del',
    'taskmeta_collection': 'taskmeta'
}
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///monsters.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

celery = make_celery(app)
db = SQLAlchemy(app)


class Results(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    data = db.Column('data', db.String(50))


@app.route('/')
def homepage():
    return 'Please go to a URL like <a href="/process/Radar">this</a> to run this program. See the README.md file in this directory.'


@app.route('/insert-data-async')
def insert_data_async():
    insert.delay()
    return 'Processing your data.'


@app.route('/insert-data')
def insert_data():
    """Sync. Holds up the browser."""
    return insert()

@app.route('/count-rows')
def count_rows():
    q = db.session.query(Results).count()
    return '<h1>{}</h1>'.format(q)


@celery.task(name='celery_example.insert')
def insert():
    """Create a long DB query."""
    for i in range(50000):
        data = ''.join([choice('ABCDE') for i in range(10)])
        result = Results(data=data)
        db.session.add(result)

    db.session.commit()

    return 'Done!'

@app.route('/create-db')
def create_db():
    """Creates a database."""
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)
