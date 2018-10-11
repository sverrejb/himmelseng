from flask import Flask, jsonify
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from models import VerseEntry

from config import Config

app = Flask(__name__)
api = Api(app)

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

VERSES = {
    1: {'tekst': 'Fylla fylla fylla fylla \n fylla fylla fylla \n fylla fylla fylla fylla fylla fylla fylla',
        'linjeforening': 'Online'},
    2: {'tekst': 'Lorem ipsum',
        'linjeforening': 'Abakus'},
    3: {'tekst': 'Dolor sit amet',
        'linjeforening': 'Delta'},
}


def abort_if_verse_doesnt_exist(verse_id):
    if verse_id not in VERSES:
        abort(404, message="Verse {} doesn't exist".format(verse_id))

parser = reqparse.RequestParser()
parser.add_argument('text')
parser.add_argument('linjeforening')


class VerseEntry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1024), index=True)
    linjeforening = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '{}'.format(self.text)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

# Verse
# show a single verse, delete a verse
class Verse(Resource):
    def get(self, verse_id):
        abort_if_verse_doesnt_exist(verse_id)
        return VERSES[verse_id]

    def delete(self, verse_id):
        abort_if_verse_doesnt_exist(verse_id)
        del VERSES[verse_id]
        return '', 204

    def put(self, verse_id):
        args = parser.parse_args()
        verse = {'text': args['text']}
        VERSES[verse_id] = verse
        return verse, 201


# VerseList
# shows all verses and lets you POST to add new verse
class VerseList(Resource):
    def get(self):
        all_verses = VerseEntry.query.all()
        return jsonify([VerseEntry.as_dict(verse) for verse in all_verses])

    def post(self):
        verse = parser.parse_args()
        verse = VerseEntry(**verse)
        db.session.add(verse)
        db.session.commit()
        return verse.as_dict(), 201


## API routing
api.add_resource(VerseList, '/api/verse')
api.add_resource(Verse, '/api/verse/<int:verse_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)