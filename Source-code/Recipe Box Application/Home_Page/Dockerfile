###TCSS600A - Independent study Project ###
### Author: Sumitha Ravindran           ###
### Recipe Box Application              ###
### Dockerfile: Home Page service       ###
### Home Page endpoint for recipe box   ###

FROM ubuntu:16.04
FROM python:3.8

MAINTAINER Your Name "******"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app
EXPOSE 5010
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
