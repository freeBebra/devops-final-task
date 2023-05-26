from flask_testing import TestCase
from project import app


class FlaskAppTestCase(TestCase):
    def create_app(self):
        return app

    def test(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
