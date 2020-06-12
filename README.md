# Enhancing-the-Reliability-of-microservices-using-ISTIO

## Tools Used:
●	Python Flask
●	Flask-Prometheus-Metrics
●	Docker Desktop
●	MySQL cloud instance
●	Google Kubernetes Engine(GKE)
●	Kubectl
●	Prometheus
●	Grafana
●	Istio
●	Istioctl
●	Postman

In this project, we have created an application “Recipe Box” composed of six microservices. Let's discuss the functionality of each microservices,

## Home Page Endpoint:
This API was designed to display a few lines related to this application. This API acts as a home page for this application. This can be performed using the HTTP GET method and this method is an idempotent method.

Eg: http://34.72.54.169:5010/  - I have deployed my services in the Kubernetes so I gave my service’s external IP address as my host name. 

## Upsert Recipe Endpoint: 
This API can be used to create a new recipe and description. We can also use this API to update the description whenever needed. This can be performed using the HTTP POST method and this method is not an idempotent method. In this endpoint, we are calling view recipe API to check whether the particular recipe that the user wants to add exists in the recipe box or not. If a recipe exists, this API updates the recipe description, else this API inserts the recipe into the recipe box.

Eg: http://104.154.110.41:9010/recipe_box/upsert
We should give input in the body section (json format)

{
    "recipe_name":"Juice",
    "recipe_description": "Add water, fruit,sugar,ice in a jar and blend everything"
}

## All Recipe List Endpoint:
We can get a particular recipe and its description by recipe name from the recipe box using this API. This can be performed using the HTTP GET method and this method is an idempotent method.

Eg: http://35.226.67.226:6010/recipe_box

## View Recipe Endpoint:
This API can be used to view all the recipes in the recipe box. This can be performed using the HTTP GET method and this method is an idempotent method.

Eg: http://35.225.105.18:7010/recipe_box/recipes?recipe_name=omelette


## Delete Recipe Endpoint:
This API was designed to delete the recipe by using the recipe name in the recipe box. This can be performed using the HTTP DELETE method and this method is an idempotent method.

Eg: http://34.72.220.199:8010/recipe_box/delete?recipe_name=juice

## Online Suggestion Endpoint:
This API was designed to get suggestions from an external API by using the recipe name as an input. This can be performed using the HTTP GET method and this method is an idempotent method.

Eg: http://34.66.162.151:9060/suggestion?recipe_name=Noodles
 

We have included the code in our python program files to find metrics for each service. We just need to include “/metrics” at the end of the service route in the URL. 

Eg: http://34.66.162.151:9060/suggestion/metrics - to find the metrics for Online Suggestion Endpoint.

Eg: http://34.72.54.169:5010/metrics - to find the metrics for Home Page Endpoint.


## Steps to run the program:
1.	Download the Source-code folder
2.	Go to the Source-code folder/Recipe Box Application/
 
 

3.	You can see folders for each service, install all the libraries mentioned in the “requirements.txt” file.
4.	Now we can run the services locally using local host(127.0.0.1) or “0.0.0.0”
5.	Create images for each service using “Dockerfile”.

Refer the docker commands given below to build, publish port, and push images
docker build -f Dockerfile -t sr/allrecipes:latest .
docker run -p 6001:6000 sr/allrecipes
docker push sr/allrecipes
 
6.	Now using the “deployment.yaml” file , deploy the services in the Kubernetes cluster.
7.	Once the services, pods, and deployments are created, we can run the service by calling the corresponding URL with the service’s external IP as the hostname. 

Refer the Kubectl commands given below to check the running pods, services, and deployments.
kubectl get pods
kubectl get node
kubectl get deployment
kubectl get services

8.	We have included a few lines in the “deployment.yaml” file to make Prometheus scrape the data metrics. Then we just need to run the prometheus server in the localhost.
9.	We need to connect our Prometheus server to the Grafana tool by adding a prometheus URL in the Grafana data source.
10.	Once everything is done, we can get our necessary graphs by writing PROMQL queries.
11.	Export the data in excel format and analyze the data.
12.	Install istio in the Kubernetes cluster and enable sidecar injection.
Command to enable sidecar injection:
kubectl label namespace default istio-injection=enabled --overwrite
Check the injection:
kubectl get namespace -L istio-injection
13.	Repeat steps 9,10,11.


                       ************  Thank you   ************ 

