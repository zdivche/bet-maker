from fastapi import FastAPI
from app.interfaces.api import bets, events

app = FastAPI()

app.include_router(bets.router)
app.include_router(events.router)