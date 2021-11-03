FROM python:3.9

RUN apt-get update && apt-get upgrade
 && apt-get install -y --no-install-recommends \
    build-essential

ADD requirements.txt /
RUN pip install -r /requirements.txt
WORKDIR /app
ADD . /app