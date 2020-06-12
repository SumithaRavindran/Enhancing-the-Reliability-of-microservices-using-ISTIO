###TCSS600A - Independent study Project ###
### Author: Sumitha Ravindran           ###
### Recipe Box Application              ###
### Service: Home Page                  ###
### Home Page endpoint for recipe box   ###
from flask import Flask
from prometheus_client import make_wsgi_app
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from flask_prometheus_metrics import register_metrics

# Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
# http://hostname:5010/

# Function
def home():
    
    return '''<h1> Your Recipe Box </h1>
<p> Save all your favourite recipes in the recipe box for future craving </p>'''

# provide app's version and deploy environment/config name to set a gauge metric
register_metrics(app, app_version="v0.1.2", app_config="staging")

# Plug metrics WSGI app to your main app with dispatcher
dispatcher = DispatcherMiddleware(app.wsgi_app, {"/metrics": make_wsgi_app()})
# Hostname and port number
run_simple(hostname="0.0.0.0", port=5010, application=dispatcher)



