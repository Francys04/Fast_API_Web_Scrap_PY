import datetime as dt
from typing import Iterator, Dict

import scraper as _scrape

import json as js

# def range of date for collect data 
def date_range(start_date: dt.date, end_date: dt.date) -> Iterator[dt.date]:
    for n in range(int((end_date - start_date).days)):
        yield start_date + dt.timedelta(n)
        
        
    #define events from html inspect web site fro key search class  
def create_events_dict() -> Dict:
    events = dict()
    start_date = dt.date(2023, 3, 4)
    end_date = dt.date(2023, 5, 15)
    
    
    # {
    #     "april" :{
    #         "1" : "some event",
    #         "2" : "another event"
    #     },
    #     "may" : "..."
    # }
    
    for date in date_range(start_date, end_date):
        month = date.strftime("%B").lower()
        if month not in events:
            events[month] = dict()


        events[month][date.day] = _scrape.events_of_the_day(month, date.day)
    
    return events

# add all information from date_range in json file
if __name__ == "__main__":
    events = create_events_dict()
    with open("events.json", mode='w', encoding="utf-8") as events_file:
        js.dump(events, events_file, ensure_ascii=False)