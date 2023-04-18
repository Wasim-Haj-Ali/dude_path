import json
from fastapi import FastAPI

from src.database_service.user_service_repo.users_repo import UsersRepo
from src.entities.User import User
from src.entities.Response import Response


app = FastAPI()

# Remember that this path is inside the docker container
with open("src/config.json") as json_file:
    config = json.load(json_file)

user_service_information = config["user_service"]


@app.get(user_service_information["health_route"])
def read_health():
    return {"status" : "ok"}



@app.get(user_service_information["get_one_route"])
def get_user(slug: str):
    
    user_repo = UsersRepo()
    
    user = user_repo.get_one(slug)
    
    if user == None:
        response = Response(status_code="204", data=[user] ,message="User None")
    
    elif user:
        response = Response(status_code="200", data=[user] ,message="User contains data")
        
    else:
        response = Response(status_code="404", data=[user] ,message="User Something unexpected")
    
    return response



@app.post(user_service_information["create_route"])
def create_user(data: dict):

    user_repo = UsersRepo()
    
    # Validate the data
    validated_user = User(**data)


    created_user = user_repo.create(validated_user)
    
    if created_user == None:
        response = Response(status_code="500", data=[created_user] ,message="Indicator None")
    
    elif created_user:
        response = Response(status_code="200", data=[created_user] ,message="Indicator created successfully")
        
    else:
        response = Response(status_code="404", data=[created_user] ,message="Indicator Something unexpected")
        
    
    return response
    

@app.post(user_service_information["authentication_route"])
def check_user_authentication(data: dict):
    
    # TODO
    # Security level 999
    return True



@app.delete(user_service_information["delete_route"])
def delete_user(slug: str):
    
    user_repo = UsersRepo()
    
    if user_repo.delete(slug):
        response = Response(status_code="200", data=[] ,message="User deleted successfully")
        return response
    
    response = Response(status_code="404", data=[] ,message="User Something unexpected")
    
    return response
