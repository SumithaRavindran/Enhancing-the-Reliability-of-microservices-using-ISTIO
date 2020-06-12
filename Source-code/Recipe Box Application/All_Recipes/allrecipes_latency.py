###TCSS600A - Independent study Project ###
###  Author: Sumitha Ravindran          ###
### Recipe Box Application              ###
### Service : All_Recipes               ###
### Endpoint to return all the recipes  ###
### and finding latency.                ###
import flask
from flask import Flask, jsonify
import simplejson as json
import pymysql
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

# Flask
app = Flask(__name__)

# A route to return all of the available recipes in our receipe_box.
@app.route('/recipe_box', methods=['GET'])
#http://hostname:6010/recipe_box
# Function
def recipe_all():

#MySQL connection
    #REGION = 'us-central1-a'
    GCP_host  = ''
    name = ""
    password = ""
    db_name = "recipeDB"
    conn = pymysql.connect(GCP_host, user=name, passwd=password, db=db_name, connect_timeout=5)
    # DB connection check
    if conn.ping(True):
        print("connected to mysql db")
    mycursor = conn.cursor()
    print("inside recipe_all")
    
#Get all the rows from receipe_box table
    query = "select * from recipe_box"
    mycursor.execute(query)
    rows = mycursor.fetchall()
    print("Total number of recipes:",mycursor.rowcount)
#close the db connection
    conn.close()
    return jsonify(rows)

# provide app's version and deploy environment/config name to set a gauge metric
register_metrics(app, app_version="v0.1.2", app_config="staging")

# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/recipe_box/metrics": make_wsgi_app()})
# hostname and portnumber
run_simple(hostname="0.0.0.0", port=6010, application=dispatcher)