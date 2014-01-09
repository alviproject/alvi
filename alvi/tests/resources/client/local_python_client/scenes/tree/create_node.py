from alvi.client.scenes.base import Scene
from alvi.client.containers.tree import Tree
from django import forms


class TreeCreateNode(Scene):
    class Form(Scene.Form):
        parents = forms.CharField(initial="0, 0, 1, 1, 4, 4")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.nodes = []

    def run(self, **kwargs):
        tree = kwargs['container']
        data_generator = kwargs['data_generator']
        options = kwargs['options']
        parents = [int(parent) for parent in options['parents'].split(',')]
        value = next(data_generator.values)
        node = tree.create_root(value=value)
        self.nodes.append(node)
        #parents = [0, 0, 1, 1, 4, 4]  # TODO this list could be passed from test case by custom form field
        for value, parent in zip(data_generator.values, parents):
            node = self.nodes[parent].children.create(value=value)
            self.nodes.append(node)
        tree.sync()

    @classmethod
    def container_class(cls):
        return Tree