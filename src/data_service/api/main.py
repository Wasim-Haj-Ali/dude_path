import json
from fastapi import FastAPI

from src.database_service.data_service_repo.indicators_repo import IndicatorsRepo



app = FastAPI()


# Remember that this path is inside the docker container
with open("src/config.json") as json_file:
    config = json.load(json_file)

data_service_information = config["data_service"]


@app.get(data_service_information["health_route"])
def read_health():
    return {"status" : "ok"}


@app.post(data_service_information["create_route"])
def create_indicator(data: dict):
    
    indicator_repo = IndicatorsRepo()
    
    created_indictor = indicator_repo.create(data)
    
    return created_indictor



@app.get(data_service_information["get_all_route"])
def get_all_indicators():
    
    indicator_repo = IndicatorsRepo()
    
    all_indicators = indicator_repo.get_all()

    return all_indicators


@app.get(data_service_information["get_one_route"])
def get_indicator(slug: str):
    
    indicator_repo = IndicatorsRepo()
    
    indicator = indicator_repo.get_one(slug)
    
    return indicator


@app.get(data_service_information["delete_route"])
def delete_indicator(slug: str):
    
    indicator_repo = IndicatorsRepo()
    
    if indicator_repo.delete(slug):
        print(f"Deleted {slug} successfuly!")
        return True
    
    return False