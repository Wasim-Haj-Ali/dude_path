# FROM python:3.11-slim

# ADD ./app/ .

# RUN pip install fastapi "uvicorn[standard]"

# CMD ["python3", "main.py"]


FROM python:3.11-slim


WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

COPY ./app /code/app

RUN pip install --upgrade -r /code/requirements.txt

CMD  ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "23000"]