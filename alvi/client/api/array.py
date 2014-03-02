from alvi.client.api.base import update_node

CONTAINER = "Array"


def create_node(pipe, id, value):
    pipe.send('create_node', (id, ), dict(
        id=id,
        value=value,
    ))

def swap_nodes(pipe, node1, node2):
    pipe.send('swap_nodes', (1, ), dict(point1=node1, point2=node2))
