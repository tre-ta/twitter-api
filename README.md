## Requirements 

* Docker: 19.03.12-ce
* docker-compose: 1.26.2

These are the versions used while building it but I'm sure almost every recent 
version of those tools will suffice.

## Deployment

**Just one step: `./start.sh`**

From a cold cache, without the needed images on the host machine, the whole
process takes about ~7 minutes. If you already have the images you'll only need
to wait for the API to build and the services to get ready, which takes about ~2
minutes.


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
issue a query to create an index pattern in Kibana. This makes the logs easily
accessible in Elasticsearch, without having to do any configuration.


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
