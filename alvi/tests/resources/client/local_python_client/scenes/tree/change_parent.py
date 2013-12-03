from alvi.tests.resources.client.local_python_client.scenes.tree.create_node import TreeCreateNode


class TreeChangeParent(TreeCreateNode):
    def run(self, tree):
        super().run(tree)
        self.nodes[4].change_parent(self.nodes[2])
        tree.sync()


if __name__ == "__main__":
    TreeChangeParent.start()