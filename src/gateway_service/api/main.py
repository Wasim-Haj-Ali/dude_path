import json
import requests as rq
from fastapi import FastAPI




app = FastAPI()


# Remember that this path is inside the docker container
with open("src/config.json") as json_file:
    config = json.load(json_file)

USER_SERVICE_INFO = config["user_service"]
DATA_SERVICE_INFO = config["data_service"] 



@app.get("/")
def read_root():
    return "********** SIMPLE FASTAPI **********"


############### HEALTH ###############
@app.get("/api/health")
def read_health():
    return {"status" : "ok"}


@app.get("/api/user/health")
def read_user_health():
    url = USER_SERVICE_INFO["base_url"] + USER_SERVICE_INFO["health_route"]
    print(url)
    print("__________________________________________________________")
    response = rq.get(url)

    content = response.json()

    return content


@app.get("/api/data/health")
def read_data_health():

    url = DATA_SERVICE_INFO["base_url"] + DATA_SERVICE_INFO["health_route"]
    print(url)
    print("__________________________________________________________")

    response = rq.get(url)

    content = response.json()

    return content




############### CREATE ###############
@app.post("/api/user/create")
def create_user(data: dict):
    
    headers = {
        "key": "value"
    }

    url = USER_SERVICE_INFO["base_url"] + USER_SERVICE_INFO["create_route"]

    response = rq.post(url, data=data, headers=headers)

    content = response.json()
    
    return content



@app.post("/api/data/create")
def create_indicator(data: dict):
    
    headers = {
        "key": "value"
    }

    url = DATA_SERVICE_INFO["base_url"] + DATA_SERVICE_INFO["create_route"]

    response = rq.post(url, data=data, headers=headers)

    content = response.json()
    
    return content




############### GET ###############
@app.get("/api/data/content")
def get_all_indicators():
    
    url = DATA_SERVICE_INFO["base_url"] + DATA_SERVICE_INFO["get_all_route"]

    response = rq.get(url)

    # content = response.json()
    content = response.content
    return content 


@app.get("/api/user/content/{slug}")
def get_indicator(slug: str):
    
    url = USER_SERVICE_INFO["base_url"] + USER_SERVICE_INFO["get_one_route"] + "/" + slug

    response = rq.get(url)

    content = response.json()
    
    return content 


@app.get("/api/data/content/{slug}")
def get_indicator(slug: str):
    
    url = DATA_SERVICE_INFO["base_url"] + DATA_SERVICE_INFO["get_one_route"] + "/" + slug

    response = rq.get(url)

    content = response.json()
    
    return content 


############### DELETE ###############
@app.get("/api/user/delete/{slug}")
def delete_indicator(slug: str):
    
    url = USER_SERVICE_INFO["base_url"] + USER_SERVICE_INFO["delete_route"] + "/" + slug

    response = rq.get(url)

    content = response.json()
    
    return content


@app.get("/api/data/delete/{slug}")
def delete_indicator(slug: str):
    
    url = DATA_SERVICE_INFO["base_url"] + DATA_SERVICE_INFO["delete_route"] + "/" + slug

    response = rq.post(url)

    content = response.json()
    
    return content