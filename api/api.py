# api.py - Simplisic Flask APP at the moment

from flask import Flask
from flask.ext.mongoalchemy import MongoAlchemy

app = Flask(__name__)

app.config['MONGOALCHEMY_DATABASE'] = 'overhear'
db = MongoAlchemy(app)

class Overhear(db.Document):
    name = db.StringField()


@app.route('/')
def hello_world():
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
