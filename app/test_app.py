import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):

    def setUp(self):
        # Create Flask test client
        self.client = app.test_client()
        self.client.testing = True

    def test_home_route(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Flask App Running", response.data)

    def test_table_html_route(self):
        response = self.client.get("/table/html/5")
        self.assertEqual(response.status_code, 200)

        expected = b"5 x 1 = 5"
        self.assertIn(expected, response.data)

    def test_invalid_table_route(self):
        response = self.client.get("/table/html/abc")
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest.main()

