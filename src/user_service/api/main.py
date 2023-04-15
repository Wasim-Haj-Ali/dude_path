import json
from fastapi import FastAPI

from src.database_service.user_service_repo.users_repo import UsersRepo


app = FastAPI()

# Remember that this path is inside the docker container
with open("src/config.json") as json_file:
    config = json.load(json_file)

user_service_information = config["user_service"]


@app.get(user_service_information["health_route"])
def read_health():
    return {"status" : "ok"}


@app.post(user_service_information["create_route"])
def create_user(data: dict):
    
    user_repo = UsersRepo()
    
    created_user = user_repo.create(data)
    
    return created_user


@app.post(user_service_information["authentication_route"])
def check_user_authentication(data: dict):
    
    # TODO
    # Security level 999
    return True




@app.get(user_service_information["get_one_route"])
def get_user(slug: str):
    
    user_repo = UsersRepo()
    
    user = user_repo.get_one(slug)
    
    return user



@app.delete(user_service_information["delete_route"])
def delete_user(slug: str):
    
    user_repo = UsersRepo()
    
    if user_repo.delete(slug):
        print(f"Deleted {slug} successfuly!")
        return True
    
    return False
