from . import base
from .base import action


class Graph(base.Container):
    template = 'spaces/graph.html'

    @classmethod
    def implementations(cls):
        return (cls, )

    @action
    def create_node(self, **kwargs):
        return kwargs

    @action
    def update_node(self, **kwargs):
        return kwargs

    @action
    def remove_node(self, **kwargs):
        return kwargs

    @action
    def create_edge(self, **kwargs):
        return kwargs

    @action
    def create_multi_marker(self, **kwargs):
        return kwargs

    @action
    def multi_marker_add_node(self, **kwargs):
        return kwargs
