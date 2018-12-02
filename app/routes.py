import random
from flask import request, jsonify, send_from_directory
from flask_basicauth import BasicAuth
from flask_expects_json import expects_json
from app import db, app
from app.models import VerseEntry


auth = BasicAuth(app)
schema = {
    'type': 'object',
    'properties': {
        'text': {'type': 'string'},
        'linjeforening': {'type': 'string'}
    },
    'required': ['text']
}


@app.route('/api/verse/<verse_id>', methods=['GET'])
def get_verse(verse_id):
    result = VerseEntry.query.get(verse_id)
    return (jsonify(result.as_dict()), 200) if result else (jsonify({}) , 404)


@app.route('/api/verse/<verse_id>', methods=['DELETE'])
@auth.required
def delete_verse(verse_id):
    VerseEntry.query.filter_by(id=verse_id).delete()
    db.session.commit()
    return jsonify({}), 204


@app.route('/api/verse/random', methods=['GET'])
def get_random_verse():
    random_id = random.randrange(0, db.session.query(VerseEntry).count())
    random_verse = db.session.query(VerseEntry)[random_id]
    return jsonify(random_verse.as_dict()), 200



@app.route('/api/verse', methods=['GET'])
def get_all_verses():
    all_verses = VerseEntry.query.all()
    return jsonify([VerseEntry.as_dict(verse) for verse in all_verses])

@app.route('/api/verse', methods=['POST'])
@expects_json(schema)
def post_verse():
    verse = VerseEntry(**request.json)
    db.session.add(verse)
    db.session.commit()
    return jsonify(verse.as_dict()), 201

@app.route('/')
def index():
    return send_from_directory('../dist/', 'index.html')


@app.route('/<path:path>', methods=['GET'])
def serve_static_files(path):
 
    if not os.path.isfile(os.path.join(static_file_dir, path)):
        path = os.path.join(path, 'index.html')
 
    return send_from_directory(static_file_dir, path)