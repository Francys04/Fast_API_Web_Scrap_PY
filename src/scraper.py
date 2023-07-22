"""allowing to add annotations to function parameters and return values to indicate the expected types of data."""
from typing import List
"""The requests library is a popular Python library used to make HTTP requests to web servers and interact with APIs."""
import requests as _request
"""Python library used for web scraping and parsing HTML and XML documents."""
from bs4 import BeautifulSoup as _bs4

"""Choose url abd acces function of url adress"""
def generate_url(month: str, day : int ) -> str:
    url = f"https://www.onthisday.com/day/{month}/{day}"
    return url

def get_page(url: str) -> _bs4:
    page = _request.get(url)
    soup = _bs4(page.content, "html.parser")
    return soup

def events_of_the_day(month: str, day: int) -> List[str]:
    """
    Return the events of a given day
    will show all data in text format by list comprihation -> termnal output by py craper.py
    """
    url = generate_url(month, day)
    page = get_page(url)
    raw_events = page.find_all(class_="event")
    events = [event.text for event in raw_events]
    # print(events)
    return events

"""enter a date for execute extract data api """
events_of_the_day("february", 24)
    

