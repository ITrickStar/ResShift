#!/bin/sh

echo "Docker build started!"

docker build -t resshift:latest .

if [ $? -eq 0 ]; then
    docker run -p 7860:7860 --gpus all -it resshift
    
    if [ $? -eq 0 ]; then
        echo "\033[0;32m Server successfully closed"
    else
        echo "\033[0;31m Error while starting resshift"
        exit 1
    fi
else
    echo "\033[0;31m  Error while building resshift"
    exit 1
fi
