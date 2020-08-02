## Overview
This project aims to collect the latest posts from Twitter and generate a few
insights, such as the most followed users and amount of hashtags per hashtag and
language. To achieve this goal, this project consumes the official Twitter API.

## Requirements 

* Docker: 19.03.12-ce
* docker-compose: 1.26.2

These are the versions used while building it but I'm sure almost every recent 
version of those tools will suffice.

## Deployment

Before the deployment begins, you'll need to set your Twitter API credentials.
More specifically, the Token Bearer for authentication. This project provides an
.env file on the root folder, all you have to do is replace it with your values:

```
BEARER_TOKEN=####  REDACTED - REPLACE THIS WITH YOUR TWITTER API BEARER  ####

ROOT_USERNAME=mongo
ROOT_PASSWORD=mongopw
ROOT_DATABASE=tweets_db
MONGO_IP=db
```


**Just one step: `./start.sh`**

From a cold cache, without the needed images on the host machine, the whole
process takes **~7 minutes**. If you already have the images you'll only need 
to wait for the API to build and the services to get ready, which takes 
**~2 minutes**. This is a time estimation, it might be longer due to slower 
connections.


This is going to run `docker-compose` on the background, creating the following
services:

* **`db`** (mongo:4.2) - used to save the tweets
* **`api`** (built from the Dockerfile at the root folder)
* **`elasticsearch`** (elasticsearch:7.8.1) - database for logs
* **`kibana`** (kibana:7.8.1) - visualization for Elasticsearch
* **`filebeat`** (filebeat:7.8.1) - responsible for gathering and serving
    Elasticsearch
* **`prometheus`** (prometheus:latest) - metrics database
* **`grafana`** (grafana:latest) - metrics visualization (dashboards)

After that, the script is going to wait for the Kibana server and then
issue a query to create an index pattern in Kibana. This makes the logs easy to 
access in Elasticsearch, without having to do any configuration.

You'll end up with the following endpoints:

* **`localhost:8000`** - API
* **`localhost:27017`** - MongoDB
* **`localhost:9200`** - Elasticsearch
* **`localhost:5601/app/kibana`** - Kibana
* **`localhost:9090`** - Prometheus
* **`localhost:3000`** - Grafana


## API

The API is built on top of [FastAPI](https://fastapi.tiangolo.com/), a "modern,
high-performance, web framework for building APIs with Python 3.6+".

There are the following endpoints:

* **`/`** to insert new data from hashtags
* **`/most-followed-users`** to get the most followed users
* **`/total-hashtag-lang`** to get the total amount of tweets ordered by hashtag
    and language
* **`/total-per-hour`** to get the total amount of tweets per hour of the day
* **`/docs`** automatically created with Swagger UI
* **`/metrics`** where the metrics are getting exposed

 
The API imports the backend class "Tweets" and then uses tweets' methods to
serve the requests. The "Tweets" class is implemented in the `tweets.py` file.

### Query examples

* `http://localhost:8000/` - inserts the default hashtags: openbanking,
remediation, devops, sre, microservices, observability, oauth, metrics,
logmonitoring and opentracing

* `http://localhost:8000/?htag=remediation&htag=openbanking` - inserts 
remediation and openbanking hashtags (if the documents are not already present)

* `http://localhost:8000/most-followed-users` - returns a list with the five
most followed users which used one of the hashtags you inserted into the
database

* `http://localhost:8000/total-per-hour` - returns a list, ordered by hour, of
the amount of tweets.

* `http://localhost:8000/total-hashtag-lang` - returns a list of the amount of
documents, organized by hashtag and language.


## Infrastructure

![infrastructure](https://github.com/tre-ta/twitter-api/blob/master/images/infrastructure.jpg)


## Logs (taken from Kibana) (localhost:5601/app/kibana)

API logs (filtered by INFO and DEBUG):

![kibana](https://github.com/tre-ta/twitter-api/blob/master/images/kibana.png)

MongoDB logs:

![mongo](https://github.com/tre-ta/twitter-api/blob/master/images/mongo.png)

Filebeat is configured to get all the logs from the host machine's containers. 
This means you have access to every aspect of the infrastructure. Even from the
filebeat service itself. The `container.image.name` helps precisely choosing 
which container you want. The logs are timefiltered as well, so you can set 
the range you want.

# Dashboard (in Grafana) (localhost:3000)

This is the Twitter API dashboard. There are four metrics being displayed:

1. Total requests by endpoint and status code
2. Latency in seconds
3. Amount of errors returned by path
4. Sum of all returned errors of all paths

![grafana-interface](https://github.com/tre-ta/twitter-api/blob/master/images/grafana-interface.png)

## Total requests by endpoint and status code

![grafana-1](https://github.com/tre-ta/twitter-api/blob/master/images/grafana-1.png)

## Latency in seconds
![grafana-2](https://github.com/tre-ta/twitter-api/blob/master/images/grafana-2.png)

## Amount of errors returned by path
![grafana-3](https://github.com/tre-ta/twitter-api/blob/master/images/grafana-3.png)

## Sum of all returned errors
![grafana-4](https://github.com/tre-ta/twitter-api/blob/master/images/grafana-4.png)

