from fastapi import FastAPI
# app/ is inside the container
from app.database import database as db 
from app.entities import Indicator

app = FastAPI()

@app.get("/")
async def read_root():
    return "********** SIMPLE FASTAPI **********"


@app.get("/api/health")
async def read_health():
    return {"status" : "ok"}


@app.post("/api/content")
async def create_indicator():   # indicator: Indicator. parameter prepared using pydantic for future use. At the moment not necessary
    
    created_indictor = await db.create_indicator()  # indicator
    
    return created_indictor

print("Finished!")



@app.get("/api/content")
async def get_all_indicators():
    
    all_indicators = await db.get_all_indicators()
    
    return all_indicators


@app.get("/api/content/{slug}")
async def get_indicators_by_slug(slug: str):
    
    indicator = await db.get_indicator_by_slug(slug)
    
    return indicator
    
