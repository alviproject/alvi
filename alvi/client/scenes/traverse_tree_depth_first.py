from alvi.client.scenes.create_tree import CreateTree


class TraverseTreeDepthFirst(CreateTree):
    def traverse(self, marker, tree, node):
        marker.append(node)
        tree.stats.traversed_nodes += 1
        tree.sync()
        for child in node.children:
            self.traverse(marker, tree, child)

    def run(self, **kwargs):
        tree = kwargs['container']
        with tree.postpone_sync():
            super().run(**kwargs)
        marker = tree.create_multi_marker("Traversed")
        tree.stats.traversed_nodes = 0
        self.traverse(marker, tree, tree.root)
