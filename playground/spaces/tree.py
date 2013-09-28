from . import base


class Tree(base.Space):
    template = "spaces/tree.html"

    def create_node(self, id, value, parent_id):
        return ('create_node', dict(
            id=id,
            value=value,
            parent_id=parent_id,
        ))

    def update_node(self, id, value):
        return ('update_node', dict(
            id=id,
            value=value,
        ))
