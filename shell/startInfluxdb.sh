#!/usr/bin/env bash

docker stop jmeterdb
docker rm jmeterdb
docker run -d -p 8086:8086 -p 8083:8083 --name=jmeterdb influxdb