#!/bin/bash

PUBLISH_FILE=docker-compose.publish.yml

docker-compose -f ${PUBLISH_FILE} build --no-cache
docker-compose -f ${PUBLISH_FILE} push

echo "Please, type the new version you want to publish (ex: 1.0)"
echo "    >Visite https://git.aiotools.ovh/aio/skeleton-project/container_registry/2"
echo ">"
read VERSION

export version=${VERSION}

docker-compose -f ${PUBLISH_FILE} build 
docker-compose -f ${PUBLISH_FILE} push