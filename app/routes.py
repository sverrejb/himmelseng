from flask_restful import Resource, reqparse
from flask_httpauth import HTTPBasicAuth
import random
from flask import jsonify
from app.models import VerseEntry
from app import db, api, app

parser = reqparse.RequestParser()
parser.add_argument('text', type=str, required=True)
parser.add_argument('linjeforening', type=str)

auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == app.config['ADMIN_USER']:
        return app.config['ADMIN_PASSWORD']
    return None


@auth.error_handler
def unauthorized():
    # return 403 instead of 401 to prevent browsers from displaying the default
    # auth dialog
    return jsonify({'message': 'Unauthorized access'}), 401


# Verse
# show a single verse
class Verse(Resource):
    def get(self, verse_id):
        result = VerseEntry.query.get(verse_id)
        return (result.as_dict(), 200) if result else ({} , 404)

# delete a verse
class DeleteVerse(Resource):
    decorators = [auth.login_required]
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
api.add_resource(DeleteVerse, '/api/verse/<int:verse_id>')
api.add_resource(Verse, '/api/verse/<int:verse_id>')
api.add_resource(RandomVerse, '/api/verse/random')
