import unittest
from typing import Dict
from services import get_all_events, get_month_events, get_events_of_day, get_of_today

class TestEvents(unittest.TestCase):
    def test_get_all_events(self):
        events = get_all_events()
        self.assertIsInstance(events, dict)
        # Add more specific assertions based on the expected structure of the data

    def test_get_month_events(self):
        month_events = get_month_events("april")
        self.assertIsInstance(month_events, Dict)
        # Add more specific assertions based on the expected structure of the data

    def test_get_month_events_invalid_month(self):
        invalid_month = get_month_events("nonexistent_month")
        self.assertEqual(invalid_month, "this month isn't real you fool")

    def test_get_events_of_day_invalid_date(self):
        invalid_date = get_events_of_day("april", 32)
        self.assertEqual(invalid_date, "Not exist the data from this date")

    def test_get_of_today(self):
        today_events = get_of_today()
        self.assertIsInstance(today_events, str)
        # Add more specific assertions based on the expected structure of the data
        
if __name__ == '__main__':
    unittest.main()