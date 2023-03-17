# FROM python:3.11-slim

# ADD ./app/ .

# RUN pip install fastapi "uvicorn[standard]"

# CMD ["python3", "main.py"]


FROM python:3.11-slim

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY . /code/app

RUN echo "Installing libraries..."

RUN pip install fastapi "uvicorn[standard]"

RUN pip install --upgrade -r /code/requirements.txt

RUN echo "Finished installing libraries!"

CMD  ["uvicorn", "app.api.main:app", "--host", "0.0.0.0", "--port", "23000"]