"""The unittest module is part of the Python Standard Library and 
provides a testing framework for writing and running unit tests."""
import unittest
from fastapi.testclient import TestClient
from main import app

"""This is approach to ensure that the endpoints in  FastAPI app are behaving as expected. 
The test contains test cases for several endpoints: /, /events, /events/today, /events/april, and /events/april/1."""
class TestApp(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def test_root(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "welcome to this historical events api"})

    def test_all_events(self):
        response = self.client.get("/events")
        self.assertEqual(response.status_code, 200)
    
    def test_events_of_today(self):
        response = self.client.get("/events/today")
        self.assertEqual(response.status_code, 200)
            

    def test_get_events_of_month(self):
        response = self.client.get("/events/april")
        self.assertEqual(response.status_code, 200)
            

    def test_get_events_of_day(self):
        response = self.client.get("/events/april/1")
        self.assertEqual(response.status_code, 200)

"""When run the script directly (not as a module imported into another script), 
this block will be executed, and the unittest.main() function will be called."""
if __name__ == "__main__":
    unittest.main()