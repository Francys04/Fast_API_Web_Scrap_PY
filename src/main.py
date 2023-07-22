from fastapi import FastAPI
"""import service as serv"""
import services as serv

app = FastAPI()

"""Defined a FastAPI application and created various API endpoints to serve 
historical events data using the functions from the services module."""
@app.get("/")
async def root():
    return{"message":"welcome to this historical events api"}


"""create entires events api"""
"""/events => This endpoint is used to retrieve all events. 
It calls the serv.get_all_events() function from the services module and returns the results as a JSON response."""
@app.get("/events")
async def all_events():
    return serv.get_all_events()

"""/events/today => This endpoint fetches events for the current date. 
It calls the serv.get_of_today() function from the services module and returns the results as a JSON response."""
@app.get("events/today")
async def events_of_today():
    return serv.get_of_today()

"""/events/{month} => This endpoint is for fetching events for a specific month. 
It takes the month as a parameter and calls the serv.get_month_events(month) function from the services module, 
returning the results as a JSON response."""
@app.get("/events/{month}")
async def get_events_of_month(month: str):
    return serv.get_month_events(month)

"""/events/{month}/{day} => This endpoint fetches events for a specific day of a specific month. 
It takes both month and day as parameters and 
calls the serv.get_events_of_day(month, day) function from the services module, returning the results as a JSON response."""
@app.get("/events/{month}/{day}")
async def get_events_of_day(month: str, day: int):
    return serv.get_events_of_day(month, day)