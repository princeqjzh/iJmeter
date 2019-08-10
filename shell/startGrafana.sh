#!/usr/bin/env bash
export grafana_name=newgrafana
docker stop $grafana_name
docker rm $grafana_name
docker run -d -p 3000:3000 --name=$grafana_name -v $grafana_volumn:/var/lib/grafana grafana/grafana