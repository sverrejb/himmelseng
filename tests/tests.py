import base64
import json
import os
import unittest

from app import db
from himmelseng import app
from base64 import b64encode

TEST_DB = 'test.db'
valid_entry = json.dumps({'text': 'lorem ipsum', 'linjeforening': 'dolor sit amet'})
invalid_entry = json.dumps({'foo': 'bar', 'baz': 'buzz'})
auth_header = {'Authorization': 'Basic ' + b64encode(
    bytes('{0}:{1}'.format(app.config['BASIC_AUTH_USERNAME'], app.config['BASIC_AUTH_PASSWORD']), 'ascii')).decode('ascii')}


class BasicTests(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
                                                os.path.join(app.config['BASEDIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()
        self.app.post('/api/verse',
                      data=valid_entry,
                      content_type='application/json')

    def tearDown(self):
        pass

    def test_ping(self):
        response = self.app.get('/api/verse', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        response = self.app.post('/api/verse',
                                 data=valid_entry,
                                 content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_post_invalid(self):
        response = self.app.post('/api/verse',
                                 data=invalid_entry,
                                 content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_get(self):
        response = self.app.get('/api/verse/1')
        self.assertEqual(response.status_code, 200)

    def test_get_404(self):
        response = self.app.get('/api/verse/99')
        self.assertEqual(response.status_code, 404)

    def test_random(self):
        response = self.app.get('/api/verse/random')
        self.assertEqual(response.status_code, 200)

    def test_delete(self):
        response = self.app.delete('/api/verse/1', headers = auth_header)
        self.assertEqual(response.status_code, 204)

    def test_delete_no_auth(self):
        response = self.app.delete('/api/verse/1')
        self.assertEqual(response.status_code, 401)


if __name__ == "__main__":
    unittest.main()
