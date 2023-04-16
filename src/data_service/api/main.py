import json
from fastapi import FastAPI

from src.database_service.data_service_repo.indicators_repo import IndicatorsRepo
from src.entities.Indicator import Indicator
from src.entities.Response import Response



app = FastAPI()


# Remember that this path is inside the docker container
with open("src/config.json") as json_file:
    config = json.load(json_file)

data_service_information = config["data_service"]


@app.get(data_service_information["health_route"])
def read_health():
    return {"status" : "ok"}





@app.get(data_service_information["get_all_route"])
def get_all_indicators():
    
    indicator_repo = IndicatorsRepo()
    
    all_indicators = indicator_repo.get_all()

    return all_indicators


# @app.get(data_service_information["get_one_route"])
@app.get("/data/indicators/{slug}")
def get_indicator(slug: str):
    
    indicator_repo = IndicatorsRepo()
    
    indicator = indicator_repo.get_one(slug)

    if indicator == None:
        response = Response(status_code="204", data=[indicator] ,message="Indicator None")
    
    elif indicator:
        response = Response(status_code="200", data=[indicator] ,message="Indicator contains data")
        
    else:
        response = Response(status_code="404", data=[indicator] ,message="Indicator Something unexpected")
    
    return response



@app.post(data_service_information["create_route"])
def create_indicator(data: dict):
    
    indicator_repo = IndicatorsRepo()
    
    # Validate the data
    validated_indicator = Indicator(**data)
    
    created_indictor = indicator_repo.create(validated_indicator)
    
    if created_indictor == None:
        response = Response(status_code="500", data=[created_indictor] ,message="Indicator None")
    
    elif created_indictor:
        response = Response(status_code="200", data=[created_indictor] ,message="Indicator created successfully")
        
    else:
        response = Response(status_code="404", data=[created_indictor] ,message="Indicator Something unexpected")
        
    
    return response



@app.patch(data_service_information["update_route"])
def update_indicator(slug:str, data: dict):
    """currently the updating way is replacing the whole object as it is not specified by dude_path specification yet"""
    
    indicator_repo = IndicatorsRepo()
    
    # checking if the indicator exists
    existed_indicator = indicator_repo.get_one(slug)
    
    # No indicator to update!
    if existed_indicator == None:
         response = Response(status_code="500", data=[updated_indicator] ,message="Indicator None")
         return response
    
    # Validate the data
    validated_indicator = Indicator(**data)
    
    updated_indicator = indicator_repo.update(validated_indicator)
    
    if updated_indicator == None:
        response = Response(status_code="500", data=[updated_indicator] ,message="Indicator None")
    
    elif updated_indicator:
        response = Response(status_code="200", data=[updated_indicator] ,message="Indicator updated successfully")
        
    else:
        response = Response(status_code="404", data=[updated_indicator] ,message="Indicator Something unexpected")
    
    return response



@app.put(data_service_information["upsert_route"])
def upsert_indicator(slug:str, data: dict):
    
    indicator_repo = IndicatorsRepo()
    
    # checking if the indicator exists
    existed_indicator = indicator_repo.get_one(slug)
    
    # if the indicator doesn't exists then create it
    if existed_indicator == None:
        response = create_indicator(data=data)
    
    # if existed then update it
    else:
        response = update_indicator(data=data)
    
    return response



@app.get(data_service_information["delete_route"])
def delete_indicator(slug: str):
    
    indicator_repo = IndicatorsRepo()
    
    if indicator_repo.delete(slug):
        response = Response(status_code="200", data=[] ,message="Indicator deleted successfully")
        return response
    
    response = Response(status_code="404", data=[] ,message="Indicator Something unexpected")
    
    return response
