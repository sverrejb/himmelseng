import os
import unittest
import json

from himmelseng import app, db

TEST_DB = 'test.db'
valid_entry = json.dumps({'text': 'lorem ipsum', 'linjeforeining': 'dolor sit amet'})
invalid_entry = json.dumps({'foo': 'bar', 'baz': 'buzz'})


class BasicTests(unittest.TestCase):

    # executed prior to each test
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



    # executed after each test
    def tearDown(self):
        pass

    # tests
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

    def test_delete(self):
        response = self.app.delete('/api/verse/1')
        self.assertEqual(response.status_code, 204)


if __name__ == "__main__":
    unittest.main()