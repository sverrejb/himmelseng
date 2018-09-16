from flask import Flask
from flask_restful import reqparse, abort, Api, Resource

app = Flask(__name__)
api = Api(app)

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
        abort(404, message="Todo {} doesn't exist".format(verse_id))

parser = reqparse.RequestParser()
parser.add_argument('tekst')
parser.add_argument('linjeforening')


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
        verse = {'tekst': args['task']}
        VERSES[verse_id] = verse
        return verse, 201


# VerseList
# shows all verses and lets you POST to add new verse
class VerseList(Resource):
    def get(self):
        return VERSES

    def post(self):
        args = parser.parse_args()
        print(args)
        verse_id = int(max(VERSES.keys())) + 1
        VERSES[verse_id] = {'tekst': args['tekst'], 'linjeforening': args['linjeforening']}
        return VERSES[verse_id], 201

##
## API routing
##
api.add_resource(VerseList, '/verses')
api.add_resource(Verse, '/verses/<int:verse_id>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)