# Welcome to my DUDE Path solution!

<br>


## Virtual Environment (venv):
___
+ Create: <br>
    ```python3 -m venv env```
+ Start: <br>
    ```source env/bin/activate```
+ Install required libs: <br>
    ```	pip install -r requirements.txt```
+ Using the created venv: <br>
    Select the venv as the python interpreter by `ctrl+shift+p` and enter `Python: Select Interpreter` and choose your venv.  

<br>

##  Commands:
___
+ Using Dockerfile to build the api:
    + Build: <br>
    `docker build -t fastapi-webserver`

    + Run: <br>
    ``` docker run -d --name fastapi-webserver -p 23000:23000 fastapi-webserver ```

+ Using docker-compose.yml:
    + Build: <br>
        `docker-compose build`
    + Run: <br>
        *aggressively* hit enter after typing `docker-compose up`.
        `docker-compose up -d`to start it in detached mode (Running in the background).
    + Status of the running containers: <br>
        `docker-compose ps`
    + Stop: <br>
        `docker-compose down`. To stop a specific running container specify the name of the container or the service.




<br>

## Explanation
___

### Dockerfile api:

+ **`FROM python:3.11-slim`**: Specifies the base image that this image should be built on top of.
+ **`WORKDIR /code`**: Specifies the working directory for subsequent instructions in the Dockerfile. In this case, it sets the working directory to `/code`.
+ **`COPY ./requirements.txt /code/requirements.txt`**: Copies files from the host machine to the container. In this case, it copies the `requirements.txt` file from the host machine to the `/code` directory in the container, and it copies all the files in the current directory on the host machine to the `/code/app` directory in the container.
+ **`RUN pip install --upgrade -r /code/requirements.txt`**: Runs a command inside the container during the build process. In this case, it runs the command `pip install --upgrade -r /code/requirements.txt`, which installs the required Python packages.
+ **`CMD["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "23000"]`**: Specifies the command that should be run when the container starts. In this case, it runs the command `uvicorn app.main:app --host 0.0.0.0 --port 23000` inside the container. This command starts the Uvicorn server and serves the fastapi app on port 23000.


### Dockerfile database:
+ **`FROM mysql:latest`**: specifies the base image that this Docker image is built on top of. In this case, the base image is the latest version of the official MySQL Docker image.
+ **`ENV password=root`**: Environment variable is used by MySQL to set the root password for the MySQL server.
+ **`COPY ./database_commands.sql /docker-entrypoint-initdb.d/`**: This copies the *database_commands.sql* file from the local directory ./ into the */docker-entrypoint-initdb.d/* directory in the Docker image. The directory name `docker-entrypoint-initdb.d` is used because it is recognized by the official MySQL Docker image as the location where it will automatically execute any SQL scripts that are placed in that directory when the container is first started up.
+ **`RUN docker build -t dude_path_database .`**: This builds the Docker image using the Dockerfile in the current directory "." and gives it the tag name `dude_path_database`.
+ **`CMD ["docker", "run", "-d", "-p", "3306:3306", "--name", "dude_path_database", "-e", "password=root", "dude_path_database"]`**: This specifies the command that should be run when a container is started from the image. In this case, the command starts a Docker container with the name `dude_path_database`, using the image `dude_path_database`. The `-d` flag runs the container in the background (detached mode), and the `-p` flag maps port 3306 in the container to port 3306 on the host machine.


### docker-compose.yml:
+ **version** : specifies the version of the Docker Compose file format to use.
+ **services**: defines the list of services to be created and run.
    + **dude_path_database**: the name of the service being defined.
        + **image**: the name of the image to use for the service.
        + **container_name**: the name to assign to the container.
        + **environment**: sets environment variables in the container at runtime. 

    + **dude_path_api**: the name of the service being defined.
        + **build**: Specifies the path to the directory containing the Dockerfile that should be used to build the Docker image for the `dude_path_api` service.
        + **container_name**: the name to assign to the container.
        + **volumes**: mounts a host directory or a named volume as a data volume inside the container. This satisfies the task: *Database and your service should be reachable from the hostmachine*. The colon "`:`" is used to separate the source and destination paths.
        + **ports**: publishes a container’s port to the host.


<br>

## Challenges:
___

+ `requirements.txt` was not reachable from the "/app/api/Dockerfile" and solved by adding a copy of the requirements.txt in the "/app/api/" folder, which is not a good solution at all.
+ `"3307:3306"` when exposing the ports, I could not choose the default port on my host machine (Error message: *ERROR: for dude_path_database  Cannot start service dude_path_database: Ports are not available: exposing port TCP 0.0.0.0:3306 -> 0.0.0.0:0: listen tcp 0.0.0.0:3306: bind: Only one usage of each socket address (protocol/network address/port) is normally permitted. ERROR: Encountered errors while bringing up the project.*).
+ `volumes: - ./app/api:/code` error message in "/errors/volumes_keyword.txt" this keyword should mount a host directory or a named volume as a data volume inside the container. This satisfies the task: *Database and your service should be reachable from the hostmachine*. The colon "`:`" is used to separate the source and destination paths.