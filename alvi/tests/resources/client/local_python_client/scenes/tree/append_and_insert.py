from alvi.tests.resources.client.local_python_client.scenes.tree.create_node import TreeCreateNode


class TreeAppendAndInsert(TreeCreateNode):
    def run(self, **kwargs):
        super().run(**kwargs)
        tree = kwargs['container']
        self.nodes[2].children.append(self.nodes[4])
        tree.sync()
        self.nodes[2].children.insert(0, self.nodes[3])
        tree.sync()
        self.nodes[2].children.append(self.nodes[5])


if __name__ == "__main__":
    TreeAppendAndInsert.start()