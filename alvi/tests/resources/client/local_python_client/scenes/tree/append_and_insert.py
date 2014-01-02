from alvi.tests.resources.client.local_python_client.scenes.tree.create_node import TreeCreateNode


class TreeAppendAndInsert(TreeCreateNode):
    def run(self, tree):
        super().run(tree)
        self.nodes[2].children.append(self.nodes[4])
        tree.sync()
        self.nodes[2].children.insert(0, self.nodes[3])
        tree.sync()
        self.nodes[2].children.append(self.nodes[5])