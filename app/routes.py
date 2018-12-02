import os
from flask import send_from_directory, jsonify
from flask_basicauth import BasicAuth
from flask_expects_json import expects_json
from app import db, app
from app.models import VerseEntry

DIST_FOLDER = '../dist/'
NOT_FOUND = ("404", 404)

@app.route('/')
def index():
    return send_from_directory(DIST_FOLDER, 'index.html')


@app.route('/<path:path>', methods=['GET'])
def serve_static_files(path):

    try:
        folder, file_ = path.split('/')
    except ValueError:
        folder = ''
        file_ = path
 
    if not os.path.isfile(os.path.join(DIST_FOLDER + folder, file_)):
        return NOT_FOUND
 
    return send_from_directory(DIST_FOLDER + folder, file_)