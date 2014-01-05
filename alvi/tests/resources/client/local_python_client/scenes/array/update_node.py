from . import create_node


class ArrayUpdateNode(create_node.ArrayCreateNode):
    def run(self, array, options):
        super().run(array, options)
        array[2] = 5
        array.sync()