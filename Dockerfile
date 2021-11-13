FROM python:3.10

RUN apt-get update
RUN apt-get -y upgrade

RUN apt-get install -y --no-install-recommends \build-essential
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r /app/requirements.txt
EXPOSE 8000

