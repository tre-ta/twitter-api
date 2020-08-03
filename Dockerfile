FROM python:3.8-alpine 

RUN apk update && apk add build-base

RUN mkdir -p /app/src
WORKDIR /app/src

COPY setup.py /app
COPY src/requirements.txt /app/src/requirements.txt

RUN pip install -r /app/src/requirements.txt

COPY src/ .
RUN pip install /app

ENTRYPOINT ["uvicorn", "api:api", "--host", "0.0.0.0"]
