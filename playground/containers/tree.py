from . import base
from .base import action
import playground.spaces.tree


class Tree(base.Container):
    @classmethod
    def implementations(cls):
        return (cls, )

    @classmethod
    def space_class(cls):
        return playground.spaces.tree.Tree

    @action
    def create_node(self, id, value, parent_id):
        return self._space.create_node(id, value, parent_id)

    @action
    def update_node(self, id, value):
        return self._space.update_node(id, value)