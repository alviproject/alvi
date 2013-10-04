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

    @action
    def create_edge(self, node1_id, node2_id):
        return self._space.create_edge(node1_id, node2_id)

    #TODO create generic solution for this kind of functions
    @action
    def create_multi_marker(self, id, name):
        return self._space.create_multi_marker(id, name)

    @action
    def multi_marker_add_item(self, id, item_id):
        return self._space.multi_marker_add_item(id, item_id)