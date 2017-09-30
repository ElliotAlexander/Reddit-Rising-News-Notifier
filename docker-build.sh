#!/bin/bash

if [ "$EUID" != 0 ]
  then echo "Run me as root!"
  exit
fi



echo "Begining build..."
echo 	## Optional newline. 
docker build . -t "reddit-notifier:RNOTIFIER"
echo "Docker build complete."
docker run -i -d -p 6080:80 -t reddit-notifier:RNOTIFIER
