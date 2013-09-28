from . import base
from .base import action
import playground.spaces


class Graph(base.Container):
    @classmethod
    def implementations(cls):
        return (cls, )

    @classmethod
    def space_class(cls):
        return playground.spaces.Graph

    @action
    def create_node(self, id, value, parent_id):
        return self._space.create_node(id, value, parent_id)