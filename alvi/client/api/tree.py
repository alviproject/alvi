from .base import create_node
from .base import update_node


def insert_child(pipe, parent_id, index, child_id):
    pipe.send('insert_child', (child_id, ), dict(
        child_id=child_id,
        parent_id=parent_id,
        index=index,
    ))


def change_root(pipe, id):
    pipe.send('change_root', (id, ), dict(
        id=id,
    ))


CONTAINER = "Tree"