#!/bin/sh

docker-compose up -d

printf "Waiting for kibana..."
until $(curl -s -X GET localhost:5601/status -I | grep -q "200 OK"); do
	printf "."
	sleep 5
done

printf "Ready!\n\nCreating filebeat-* index pattern to visualize logs\n\n"
curl -X POST -H "kbn-xsrf: true" -H "Content-Type: application/json" -d \
	@queries/index_pattern.json localhost:5601/api/saved_objects/index-pattern/
printf "\n"
