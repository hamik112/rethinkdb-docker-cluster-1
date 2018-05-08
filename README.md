# bootstrap rethinkdb cluster

nodes:
 - rdb1 (cluster node)
 - rdb2 (cluster node)
 - rdbp (proxy node)

build container:

```
docker build -t rdb/
```

Run the compose file
```
docker-compose up
```

navigate to url http://proxy_node_ip:28010/
