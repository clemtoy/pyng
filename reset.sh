#!/bin/bash

source .env

echo "Removing previous images and containers..."
project=$(basename $(pwd))_
docker rm -f $(docker ps -aq)
docker rmi -f ${project}server
docker rmi -f ${project}backend
docker rmi -f ${project}db

if [ "$TEST_MODE" = "true" ]; then
    echo "Removing previous volumes..."
    docker volume ls | awk '$1 == "local" { print $2 }' | xargs --no-run-if-empty docker volume rm
    sudo rm -rf $DB_PATH
fi

echo "Building containers..."
docker-compose build

echo "Running containers..."
docker-compose up -d

echo "Logs:"
docker-compose logs --follow