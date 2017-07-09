#!/bin/sh

project=$(basename $(pwd))_

docker rm -f $(docker ps -aq)
docker rmi -f ${project}server
docker rmi -f ${project}backend
docker rmi -f ${project}db
docker volume ls | awk '$1 == "local" { print $2 }' | xargs --no-run-if-empty docker volume rm
sudo rm -rf db/data

docker-compose build
docker-compose up -d

docker-compose logs --follow