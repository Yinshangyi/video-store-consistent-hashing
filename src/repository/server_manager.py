import bisect
import hashlib
from typing import Dict, List


class ServerManager:
    def __init__(self, nodes=None, replicas: int=5):
        self.replicas: int = replicas

        # Dictionary representing the circles
        self.ring: Dict[int, str] = {}

        # Sorted array representing all the virtual nodes on the conceptual circle
        self.sorted_keys: List[int] = []

        if nodes:
            for node in nodes:
                self.add_node(node)

    def add_node(self, node: str):
        for i in range(self.replicas):
            virtual_node_name = f"{node}:{i}"
            key = self._hash(virtual_node_name)
            self.ring[key] = node
            bisect.insort(self.sorted_keys, key)

    def remove_node(self, node: str):
        for i in range(self.replicas):
            virtual_node_name = f"{node}:{i}"
            key = self._hash(virtual_node_name)
            self.ring.pop(key)
            self.sorted_keys.remove(key)

    def get_node(self, key: str) -> str:
        hash_val = self._hash(key)
        idx = bisect.bisect(self.sorted_keys, hash_val) % len(self.sorted_keys)
        return self.ring[self.sorted_keys[idx]]

    def _hash(self, key: str) -> int:
        return int(hashlib.md5(key.encode()).hexdigest(), 16)
