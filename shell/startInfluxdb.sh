#!/usr/bin/env bash
export influxdb_name=newinfluxdb
docker stop $influxdb_name
docker rm $influxdb_name
docker run -d -p 8086:8086 -p 8083:8083 -p 2003:2003 --name=$influxdb_name -v $influxdb_volumn:/var/lib/influxdb influxdb