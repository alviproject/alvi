from . import create_node


class ArrayUpdateNode(create_node.ArrayCreateNode):
    def run(self, array):
        super().run(array)
        array[2] = 5
        array.sync()