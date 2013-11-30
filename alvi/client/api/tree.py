from .base import create_node
from .base import update_node


def change_parent(pipe, id, parent_id):
    pipe.send('change_parent', (id, ), dict(
        id=id,
        parent_id=parent_id,
    ))


def change_root(pipe, id):
    pipe.send('change_root', (id, ), dict(
        id=id,
    ))


CONTAINER = "Tree"