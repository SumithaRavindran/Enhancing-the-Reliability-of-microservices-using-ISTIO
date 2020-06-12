###TCSS600A - Independent study Project            ###
###  Author: Sumitha Ravindran                     ###
### Recipe Box Application                         ###
### Service: online suggestion                     ###
### Endpoint to get online suggestion for recipes  ###

import requests
import json
import objectpath
import flask
from flask import Flask, request, jsonify
import simplejson as json
import pymysql
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

#Flask
app = Flask(__name__)

@app.route('/suggestion', methods=['GET'])
#http://hostname:9060/suggestion?recipe_name=Noodles

def EWS():
    param = request.args
    recipe = param.get('recipe_name')

# calling external api
    url = "https://edamam-recipe-search.p.rapidapi.com/search"

    querystring = {"q":"%s"% recipe}

    headers = {
        'x-rapidapi-host': "edamam-recipe-search.p.rapidapi.com",
        'x-rapidapi-key': "1d07f95f3dmsh4a57b630c6101efp10baf0jsne78aed223839"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    X = response.text
    Y = json.loads(X)
    jsonnn_tree = objectpath.Tree(Y['hits'])
    # extracting only neccessary data from the api
    tuple1 = tuple(jsonnn_tree.execute('$..ingredientLines'))
    tuple2 = tuple(jsonnn_tree.execute('$..ingredients'))
    
    res = {"ingredientsLines": [ x for x in tuple1 ],"ingredients":[ x for x in tuple2 ] }
    print (json.dumps(res))  
    return json.dumps(res)

# provide app's version and deploy environment/config name to set a gauge metric
register_metrics(app, app_version="v0.1.2", app_config="staging")

# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/suggestion/metrics": make_wsgi_app()})

# hostname and port number details
run_simple(hostname="0.0.0.0", port=9060, application=dispatcher)