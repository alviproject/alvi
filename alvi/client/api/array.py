from alvi.client.api.base import update_node

CONTAINER = "Array"


def create_node(pipe, id, value):
    pipe.send('create_node', (id, ), dict(
        id=id,
        value=value,
    ))
