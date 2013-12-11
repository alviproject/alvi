from alvi.tests.resources.client.local_python_client.scenes.tree.create_node import TreeCreateNode


class TreeChangeRoot(TreeCreateNode):
    def run(self, tree):
        super().run(tree)
        tree.root = self.nodes[1]
        tree.sync()
