#!/bin/bash

#
# Get live dashboard with container stats.
#
docker stats $(docker inspect --format='{{.Name}}' $(docker ps -q))
