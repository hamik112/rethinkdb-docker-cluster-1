# Bootstrap rethinkdb cluster

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

navigate to url http://127.0.0.1:28010/

```

Use the bootstrap script to create a database with 2 shards and 1 replica per shard

```
python -m pip install rethinkdb
python bootstrap.py
```

## Prerequisites

- docker version >=18.03
- docker-compose >=1.21.0
