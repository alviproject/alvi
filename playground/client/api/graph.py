from .base import create_node
from .base import update_node

CONTAINER = "Graph"


def create_edge(pipe, node1_id, node2_id):
    pipe.send('create_edge', (node1_id, node2_id), dict(
        node1_id=node1_id,
        node2_id=node2_id,
    ))
