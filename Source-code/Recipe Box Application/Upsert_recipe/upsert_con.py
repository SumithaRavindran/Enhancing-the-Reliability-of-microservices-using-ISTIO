###TCSS600A - Independent study Project       ###
###  Author: Sumitha Ravindran                ###
### Recipe Box Application                    ###
### Service: Upsert_Recipe                    ###
### Endpoint to upsert a recipe in recipe_box ###
import flask
from flask import Flask, request, jsonify
import simplejson as json
import pymysql
import requests
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

# Flask
app = Flask(__name__)

@app.route('/recipe_box/upsert', methods=['POST'])
# http://hostname:9010/recipe_box/upsert/(json input in body section)
# Function
def upsert():
    #MySQL connection
    #REGION = 'us-central1-a'
    GCP_host  = ''
    name = ""
    password = ""
    db_name = ""
    conn = pymysql.connect(GCP_host, user=name, passwd=password, db=db_name, connect_timeout=5)

    if conn.ping(True):
        print("connected to mysql db")

    mycursor = conn.cursor()
    # Input in the form of json in the body section
    param = json.loads(request.data)
    recipe_n = param.get('recipe_name')
    recipe_d = param.get('recipe_description')
    # Calling view recipe url to check the recipe is in recipe box or not
    response = requests.get("http://35.225.105.18:7010/recipe_box/recipes?recipe_name=%s" % recipe_n) #simple GET req
    res1 = response.text
    res2 = response.status_code
    print(res1)
    print(res2)
    if res2 == 200:
        # If recipe is not there, then insert the recipe using insert query
        if res1 == '{}':
            insert_query = f"""insert into recipe_box values('{recipe_n}','{recipe_d}')"""
            mycursor.execute(insert_query)
            conn.commit()
            print("inserted")  
        # Else update the recipe with the input using update query
        else:
            update_query = f"""update recipe_box set recipe_description='{recipe_d}' where recipe_name='{recipe_n}'"""
            mycursor.execute(update_query)
            conn.commit()
            print("updated")
    else:
        print(res2)

    conn.close()
    return ("Number of rows affected: '{}'".format(mycursor.rowcount))


# provide app's version and deploy environment/config name to set a gauge metric
register_metrics(app, app_version="v0.1.2", app_config="staging")

# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/recipe_box/upsert/metrics": make_wsgi_app()})

# hostname and port number details
run_simple(hostname="0.0.0.0", port=9010, application=dispatcher)