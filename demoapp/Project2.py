from fastapi import FastAPI
# from pydantic import BaseModel


app = FastAPI

BIKE = ["Styu"]


@app.get("/bike")
def get_bike():
    return BIKE