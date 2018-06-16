from flask import Flask
from flask_celery import make_celery

app = Flask(__name__)
app.config['CELERY_BROKER_URL'] = 'ampq://localhost//'
app.config['CELERY_RESULT_BACKEND'] = 'mongodb://localhost/'
app.config['CELERY_MONGODB_BACKEND_SETTINGS'] = {
    'database': 'celery_result_backend_del',
    'taskmeta_collection': 'taskmeta'
}

celery = make_celery(app)

@app.route('/process/<name>')
def process(name):
    return name


if __name__ == '__main__':
    app.run(debug=True)
