###TCSS600A - Independent study Project       ###
###  Author: Sumitha Ravindran                ###
###  Recipe Box Application                   ###
###  Dockerfile: View_a_Recipe                ###
### Endpoint to view a recipe from recipe_box ###

FROM ubuntu:16.04
FROM python:3.8

MAINTAINER Your Name "*****"

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache

COPY ./requirements.txt /recipeapp/requirements.txt

WORKDIR /recipeapp

RUN pip install -r requirements.txt

COPY . /recipeapp

EXPOSE 7010
ENTRYPOINT [ "python" ]

CMD [ "viewrecipe_latency.py" ]