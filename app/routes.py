import os
from flask import send_from_directory, jsonify
from flask_basicauth import BasicAuth
from flask_expects_json import expects_json
from app import app

STATIC_ROOT = '../dist/'
NOT_FOUND = ("404", 404)

@app.route('/')
def index():
    return send_from_directory(STATIC_ROOT, 'index.html')


@app.route('/<path:path>', methods=['GET'])
def serve_static_files(path):

    try:
        folder, file_ = path.split('/')
    except ValueError:
        folder = ''
        file_ = path
 
    if not os.path.isfile(os.path.join(STATIC_ROOT + folder, file_)):
        return NOT_FOUND
 
    return send_from_directory(STATIC_ROOT + folder, file_)