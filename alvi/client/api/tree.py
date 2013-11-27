from .base import create_node
from .base import update_node


def change_parent(pipe, id, parent_id):
    pipe.send('change_parent', (id, ), dict(
        id=id,
        parent_id=parent_id,
    ))


CONTAINER = "Tree"