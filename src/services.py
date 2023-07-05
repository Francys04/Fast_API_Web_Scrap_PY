from typing import Dict
import json
import datetime as dt


def get_all_events() -> Dict:
    with open("events.json", encoding="utf8") as events_file:
        data = json.load(events_file)
        
    return data


def get_month_events(month: str) -> Dict:
    events = get_all_events()
    try:
        month_events = events[month]
        return month_events
    except KeyError:
        return "this month isn't real you fool"
    
    
def get_events_of_day(month: str, day: int) -> Dict:
    events = get_all_events()
    month = month.lower()
    try:
        events = events[month][str(day)]
        return events
    except KeyError:
        return "Not exist the data from this date"
    
    
    
def get_of_today():
    today = dt.date.today()
    month = today.strftime("%B")
    return get_events_of_day(month, today.day)