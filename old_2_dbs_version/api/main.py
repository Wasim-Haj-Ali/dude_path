from fastapi import FastAPI
from src.database.database import Database

app = FastAPI()

@app.get("/")
def read_root():
    return "********** SIMPLE FASTAPI **********"


@app.get("/api/health")
def read_health():
    return {"status" : "ok"}


@app.post("/api/content")
def create_indicator(data: dict):
    
    db = Database(database="dude_path_database", table="indicators")
    
    created_indictor = db.create_indicator(data)
    
    return created_indictor

print("Finished!")



@app.get("/api/content")
def get_all_indicators():
    
    db = Database(database="dude_path_database", table="indicators")
    
    all_indicators = db.get_all_indicators()

    return all_indicators


@app.get("/api/content/{slug}")
def get_indicator(slug: str):
    
    db = Database(database="dude_path_database", table="indicators")
    
    indicator = db.get_indicator(slug)
    
    return indicator


@app.get("/api/content/delete/{slug}")
def delete_indicator(slug: str):
    
    db = Database(database="dude_path_database", table="indicators")
    
    if db.delete_indicator(slug):
        return f"Deleted {slug} successfuly!"
    
    return "Something went wrong"