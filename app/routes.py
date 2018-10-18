from flask_restful import Resource, reqparse
import random
from flask import jsonify
from app.models import VerseEntry
from app import db, api

parser = reqparse.RequestParser()
parser.add_argument('text', type=str, required=True)
parser.add_argument('linjeforening', type=str)


# Verse
# show a single verse, delete a verse
class Verse(Resource):
    def get(self, verse_id):
        result = VerseEntry.query.get(verse_id)
        return (result.as_dict(), 200) if result else ({} , 404)

    def delete(self, verse_id):
        VerseEntry.query.filter_by(id=verse_id).delete()
        db.session.commit()
        return {}, 204


class RandomVerse(Resource):
    def get(self):
        random_id = random.randrange(0, db.session.query(VerseEntry).count())
        random_verse = db.session.query(VerseEntry)[random_id]
        return random_verse.as_dict(), 200


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


# API routing
api.add_resource(VerseList, '/api/verse')
api.add_resource(Verse, '/api/verse/<int:verse_id>')
api.add_resource(RandomVerse, '/api/verse/random')
