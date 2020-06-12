###TCSS600A - Independent study Project         ###
###  Author: Sumitha Ravindran                  ###
### Recipe Box Application                      ###
### Service: Delete_a_Recipe                    ###
### Endpoint to delete a recipe from recipe_box ###
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

@app.route('/recipe_box/delete', methods=['DELETE'])
# http://hostname:8010/recipe_box/delete?recipe_name=Coffee

# function
def delete_recipe():
    #MySQL connection
    #REGION = 'us-central1-a'
    GCP_host  = ''
    name = ""
    password = ""
    db_name = "recipeDB"
    conn = pymysql.connect(GCP_host, user=name, passwd=password, db=db_name, connect_timeout=5)

    if conn.ping(True):
        print("connected to mysql db")
    # getting input from user
    mycursor = conn.cursor()
    del_param = request.args
    del_recipe = del_param.get('recipe_name')

    print (del_recipe)
    # delete query
    del_query = f"""delete from recipe_box where recipe_name ='{del_recipe}'"""
    mycursor.execute(del_query)
    conn.commit()
    #close the db connection
    conn.close() 
  
    return ("Number of rows affected: '{}'".format(mycursor.rowcount))

# provide app's version and deploy environment/config name to set a gauge metric
register_metrics(app, app_version="v0.1.2", app_config="staging")

# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/recipe_box/delete/metrics": make_wsgi_app()})

# hostname and port number
run_simple(hostname="0.0.0.0", port=8010, application=dispatcher)
