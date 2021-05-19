import unittest
from io import BytesIO

from flask_testing import TestCase
from app import App


class ApiTests(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def create_app(self):
        self.app = App().init()
        self.client = self.app.test_client()
        # self.baseURL = "http://localhost:5000/api/test_api"
        return self.app

    def test_api_get(self):
        print('Testing get request')
        rv = self.client.get('/api/data_store')
        # assert rv.status_code == 200
        self.assertEqual(rv.status_code, 200)

    def test_api_post(self):
        print('Testing post request')
        rv = self.client.post('/api/data_store',
                              # File parameter: (Input file name/path, output file name)
                              data=dict(name='User',
                                        file=('', 'test.csv')),
                              content_type='multipart/form-data')
        # assert rv.status_code == 200
        self.assertEqual(rv.status_code, 200)


if __name__ == '__main__':
    unittest.main()
