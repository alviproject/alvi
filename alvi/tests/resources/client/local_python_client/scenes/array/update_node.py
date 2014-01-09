from . import create_node


class ArrayUpdateNode(create_node.ArrayCreateNode):
    def run(self, **kwargs):
        super().run(**kwargs)
        array = kwargs['container']
        array[2] = 5
        array.sync()