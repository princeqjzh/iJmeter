#!/usr/bin/env bash
docker stop mygrafana
docker rm mygrafana
docker run -d -p 3000:3000 --name=mygrafana -v $grafana_volumn:/var/lib/grafana grafana/grafana