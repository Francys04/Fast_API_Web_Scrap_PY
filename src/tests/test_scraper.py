import pytest
from src.scraper import generate_url, get_page, events_of_the_day

"""This test ensures that the generate_url() function generates the correct URL based on the given month and day inputs. 
It checks that the returned URL matches the expected URL for the given input."""
def test_generate_url():
    url = generate_url("february", 24)
    assert url == "https://www.onthisday.com/day/february/24"

"""This test checks if the get_page() function returns a valid result, when given a valid URL. 
This ensures that the function is able to fetch the web page content successfully."""
def test_get_page():
    url = "https://www.onthisday.com/day/february/24"
    soup = get_page(url)
    assert soup is not None

"""This test verifies that the events_of_the_day() function returns a list of events for the given month and day. 
It checks that the returned events variable is a list, 
has a length greater than zero (not empty) and that all elements in the list are strings (events)."""
def test_events_of_the_day():
    events = events_of_the_day("february", 24)
    assert isinstance(events, list)
    assert len(events) > 0
    assert all(isinstance(event, str) for event in events)
    
