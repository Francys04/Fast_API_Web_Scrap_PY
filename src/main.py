from fastapi import FastAPI
# import service
import services as serv

app = FastAPI()

@app.get("/")
async def root():
    return{"message":"welcome to this historical events api"}


# create entires events api
@app.get("/events")
async def all_events():
    return serv.get_all_events()


@app.get("events/today")
async def events_of_today():
    return serv.get_of_today()


@app.get("/events/{month}")
async def get_events_of_month(month: str):
    return serv.get_month_events(month)


@app.get("/events/{month}/{day}")
async def get_events_of_day(month: str, day: int):
    return serv.get_events_of_day(month, day)