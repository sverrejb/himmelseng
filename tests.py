import os
import unittest
import json

from himmelseng import app, db

TEST_DB = 'test.db'
valid_entry = json.dumps({'text': 'foo', 'linjeforeining': 'bar'})


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


    # executed after each test
    def tearDown(self):
        pass

    # tests
    def test_ping(self):
        response = self.app.get('/api/verse', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    #TODO: Test insertion of verse
    def test_create(self):
        response = self.app.post('/api/verse',
                                 data=valid_entry,
                                 content_type='application/json')

        self.assertEqual(response.status_code, 201)

    #TODO: Test read of verse
    def test_read(self):
        pass

    #TODO: Test deletion of verse
    def test_delete(self):
        pass


if __name__ == "__main__":
    unittest.main()