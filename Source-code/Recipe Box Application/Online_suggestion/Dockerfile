###TCSS600A - Independent study Project            ###
###  Author: Sumitha Ravindran                     ###
### Recipe Box Application                         ###
### Dockerfile: online suggestion                  ###
### Endpoint to get online suggestion for recipes  ###

FROM ubuntu:16.04
FROM python:3.8

MAINTAINER Your Name "******"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /recipeapp/requirements.txt

WORKDIR /recipeapp

RUN pip install -r requirements.txt

COPY . /recipeapp

EXPOSE 9060
ENTRYPOINT [ "python" ]

CMD [ "suggestion_latency.py" ]
