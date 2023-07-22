""" It is used to indicate that a particular function parameter or 
return value is expected to be a dictionary with specific key-value pairs."""
from typing import Dict
"""JSON is a lightweight data interchange format that is easy for humans 
to read and write and easy for machines to parse and generate."""
import json
"""The datetime module provides classes for working with dates and times in Python."""
import datetime as dt


"""This function reads the data from the "events.json" file and returns it as a Python dictionary. 
The json.load() method is used to load the JSON data into a Python dictionary. 
The returned data represents all historical events."""
def get_all_events() -> Dict:
    with open("events.json", encoding="utf8") as events_file:
        data = json.load(events_file)
        
    return data

"""Get all events, then extracts events for the specified month from the data. 
If the month is found in the data, it returns the events for that month as a dictionary. 
If the month is not found, it returns a string indicating that the month isn't valid."""
def get_month_events(month: str) -> Dict:
    events = get_all_events()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "this month isn't real you fool"
    

"""Get all events, then extracts events for the specified month and day. 
If the month and day are found in the data, it returns the events for that day as a dictionary. 
If either the month or day is not found, it returns a string indicating that the data for that date doesn't exist."""    
def get_events_of_day(month: str, day: int) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        events = events[month][str(day)]
        return events
    except KeyError:
        return "Not exist the data from this date"
    
    
"""Get the current date and then calls get_events_of_day() to get the events for today."""
def get_of_today():
    today = dt.date.today()
    month = today.strftime("%B")
    return get_events_of_day(month, today.day)