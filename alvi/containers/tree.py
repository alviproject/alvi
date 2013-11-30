from . import base
from .base import action


class Tree(base.Container):
    template = 'spaces/tree.html'

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
    def change_parent(self, **kwargs):
        return kwargs

    @action
    def change_root(self, **kwargs):
        return kwargs