FROM python:3.11-slim

WORKDIR /dude_path_app

COPY ./requirements.txt /dude_path_app/requirements.txt

COPY . /dude_path_app/src

RUN echo "Installing libraries..."

RUN pip install fastapi "uvicorn[standard]"

RUN pip install --upgrade -r /dude_path_app/requirements.txt

RUN echo "Finished installing libraries!"

CMD  ["uvicorn", "src.data_service.api.main:app", "--host", "0.0.0.0", "--port", "23002"]