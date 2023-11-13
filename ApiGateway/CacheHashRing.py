import json

import redis
from uhashring import HashRing


class CacheHashRing:
    def __init__(self, nodes):
        self.ring = HashRing(nodes)
        self.nodes = nodes

    def _get_redis_client(self, key):
        node = self.ring.get_node(key)
        return redis.Redis(host=self.nodes[node]['host'], port=self.nodes[node]['port'])

    def set(self, key, value):
        client = self._get_redis_client(key)
        client.set(key, json.dumps(value), ex=30)

    def get(self, key):
        client = self._get_redis_client(key)
        value = client.get(key)
        return json.loads(value.decode()) if value else None

    def delete(self, key):
        client = self._get_redis_client(key)
        client.delete(key)
