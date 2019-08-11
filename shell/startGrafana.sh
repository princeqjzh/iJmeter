#!/usr/bin/env bash

docker stop jmeterGraf
docker rm jmeterGraf
docker run -d -p 3000:3000 --name=jmeterGraf grafana/grafana