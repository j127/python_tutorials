from flask import Flask
from flask_celery import make_celery
from time import sleep
from random import uniform
import mongoengine as mongo

mongo.connect(host='mongodb://localhost/celery_tutorial')


class Reversal(mongo.Document):
    """Represents a string and it's reversed version."""
    original = mongo.StringField(required=True)
    reversed = mongo.StringField(required=True)


app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'amqp://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'mongodb://localhost/'
app.config['CELERY_MONGODB_BACKEND_SETTINGS'] = {
    'database': 'celery_result_backend_del',
    'taskmeta_collection': 'taskmeta'
}

celery = make_celery(app)


@app.route('/')
def homepage():
    return 'Please go to a URL like <a href="/process/Radar">this</a> to run this program. See the README.md file in this directory.'


@app.route('/process/<name>')
def process(name):
    output = '''
    <p>Processing the string: {s}</p><h2>Previous Results</h2>
    '''.format(s=name)
    reverse.delay(name)
    for doc in Reversal.objects:
        output += '<li>{} => {}</li>'.format(
                doc.original, doc.reversed)
    return output


@celery.task(name='celery_example.reverse')
def reverse(string):
    r = Reversal()
    r.original = string
    sleep(uniform(1, 4))
    reversed = string[::-1]
    r.reversed = reversed
    r.save()
    return 'saved: {} => {}'.format(string, reversed)


if __name__ == '__main__':
    app.run(debug=True)
