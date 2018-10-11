import os
import unittest

from himmelseng import app, db

TEST_DB = 'test.db'


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
    def test_main_page(self):
        response = self.app.get('/api/verse', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    #TODO: Test insertion of verse
    def test_create(self):
        pass

    #TODO: Test read of verse
    def test_read(self):
        pass

    #TODO: Test deletion of verse
    def test_delete(self):
        pass


if __name__ == "__main__":
    unittest.main()