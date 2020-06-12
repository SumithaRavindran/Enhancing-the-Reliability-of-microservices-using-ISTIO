###TCSS600A - Independent study Project       ###
###  Author: Sumitha Ravindran                ###
###  Recipe Box Application                   ###
### Service: View_a_Recipe                    ###
### Endpoint to view a recipe from recipe_box ###
import flask
from flask import Flask, request, jsonify
import simplejson as json
import pymysql
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics


# Flask
app = Flask(__name__)

@app.route('/recipe_box/recipes', methods=['GET'])
# http://hostname:7010/recipe_box/recipes?recipe_name=Coffee

# Function
def recipe_needed():

    #MySQL connection
    #REGION = 'us-central1-a'
    GCP_host  = ''
    name = ""
    password = ""
    db_name = ""
    conn = pymysql.connect(GCP_host, user=name, passwd=password, db=db_name, connect_timeout=5)

    # DB connection check
    if conn.ping(True):
        print("connected to mysql db")
    mycursor = conn.cursor()

    print("inside recipe_needed")
    # Getting input as an argument from user
    param = request.args
    recipe = param.get('recipe_name')
    print (recipe)
    # SQL query
    query = f"""select * from recipe_box where recipe_name ='{recipe}'"""
    mycursor.execute(query)
    recs = mycursor.fetchall()
    conn.close() 
    # Closing db connection

## Showing the data
    for rec in recs:
        print(rec)
    return jsonify(recs)

# provide app's version and deploy environment/config name to set a gauge metric
register_metrics(app, app_version="v0.1.2", app_config="staging")

# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/recipe_box/recipes/metrics": make_wsgi_app()})

# hostname and port number
run_simple(hostname="0.0.0.0", port=7010, application=dispatcher)