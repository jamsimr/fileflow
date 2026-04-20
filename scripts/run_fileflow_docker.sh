#!/bin/bash

echo "Running FileFlow in Docker..."

docker build -t fileflow .
docker run --rm -v "$(pwd)/data:/app/data" fileflow
