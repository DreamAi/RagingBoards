#!/bin/bash

echo "Deploying to free-tier cloud..."

docker build -t raging-boards .
docker tag raging-boards raging-boards:latest

echo "Push to your cloud registry manually if needed"

echo "Deploy with:"
echo "kubectl apply -f infra/k8s/"

echo "Cloud deployment ready"
