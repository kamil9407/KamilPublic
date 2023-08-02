FROM python:3.9

RUN apt-get update && apt-get install -y mc

WORKDIR /code/

COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
