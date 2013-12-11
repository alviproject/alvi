from alvi.tests.resources.client.local_python_client.scenes.tree.create_node import TreeCreateNode


class TreeMarker(TreeCreateNode):
    def run(self, tree):
        super().run(tree)
        #TODO removing marker0 variable causes test to fail
        #looks like pipe message (see api.Pipe) is garbage collected too soon
        #it is worth to investigate that... someday
        marker0 = tree.create_marker("marker 0", self.nodes[2])
        marker1 = tree.create_marker("marker 1", self.nodes[3])
        tree.sync()
        marker1.move(self.nodes[1])
        tree.sync()