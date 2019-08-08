#!/usr/bin/env bash
docker stop myinfluxdb
docker rm myinfluxdb
docker run -d -p 8086:8086 -p 8083:8083 -p 2003:2003 --name=myinfluxdb -v $influxdb_volumn:/var/lib/influxdb influxdb