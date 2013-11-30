import alvi.client.api.tree as tree
from alvi.tests.resources.client.local_python_client.scenes.tree.create_node import TreeCreateNode


class TreeChangeRoot(TreeCreateNode):
    def run(self, pipe):
        super().run(pipe)
        tree.change_root(pipe, id=1)
        pipe.sync()


if __name__ == "__main__":
    TreeChangeRoot.start()