import os
import json
import requests
import unittest

from main import app
from dotenv import load_dotenv


class TestApp(unittest.TestCase):
    def setUp(self):
        app.config['WTF_CSRF_ENABLED'] = False
        self.client = app.test_client()

        load_dotenv()
        api_key = os.environ["MOVIE_API_KEY"]
        self.headers = {
            "accept": "application/json",
            "Authorization": f"Bearer {api_key}"
        }

    def test_hello_world(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_api(self):
        url = "https://api.themoviedb.org/3/authentication"
        response = requests.get(url, headers=self.headers)
        response_object = json.loads(response.text)

        self.assertEqual(response_object["status_code"], 1)
        self.assertEqual(response_object["success"], True)


if __name__ == "__main__":
    unittest.main()
