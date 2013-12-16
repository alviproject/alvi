from alvi.tests.resources.client.local_python_client.scenes.tree.create_node import TreeCreateNode


class TreeMultiMarker(TreeCreateNode):
    def run(self, tree):
        super().run(tree)
        marker = tree.create_multi_marker("multi marker")
        tree.sync()
        marker.append(self.nodes[0])
        marker.append(self.nodes[1])
        marker.append(self.nodes[3])
        marker.remove(self.nodes[1])
        tree.sync()