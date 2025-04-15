from tests.system.base_test import BaseTest
import json


class TestHome(TestCase):
    def setUp(self):
        pass
    
    def test_home(self):
        with self.app() as c: #self.appは base_test.pyの self.app = app.test_client
            resp = c.get('/')

            self.assertEqual(resp.status_code, 200)
            self.assertEqual(resp.json.loads(resp.get_data()), {'message': 'Hello, world!'})
    
    def test_home(self):
    with app.test_client() as c:
        resp = c.get('/')

        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json.loads(resp.get_data()), {'message': 'Hello, world!'})

