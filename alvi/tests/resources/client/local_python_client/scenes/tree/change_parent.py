import alvi.client.api.tree as tree
from alvi.tests.resources.client.local_python_client.scenes.tree.create_node import TreeCreateNode


class TreeChangeParent(TreeCreateNode):
    def run(self, pipe):
        super().run(pipe)
        tree.change_parent(pipe, id=4, parent_id=2)
        pipe.sync()


if __name__ == "__main__":
    TreeChangeParent.start()