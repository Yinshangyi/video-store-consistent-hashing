#!/bin/bash

# Define the image and container names
IMAGE_NAME="video-consistent-hashing"
CONTAINER_NAME="video-consistent-hashing"

if [[ "$(docker images -q $IMAGE_NAME 2> /dev/null)" == "" ]]; then
  echo "Image does not exist. Building the Docker image..."
  docker build -t $IMAGE_NAME .
else
  echo "Image already exists."
fi

# Run the Docker container
echo "Running the Docker container..."
docker run -p 5000:5000 --name $CONTAINER_NAME $IMAGE_NAME
