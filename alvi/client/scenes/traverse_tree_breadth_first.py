from alvi.client.scenes.create_tree import CreateTree
from collections import deque


class TraverseTreeBreadthFirst(CreateTree):
    def traverse(self, tree, node, traversed_marker, frontier_marker):
        frontier = deque()
        frontier.append(node)
        frontier_marker.append(node)
        tree.sync()
        while frontier:
            node = frontier.popleft()
            frontier_marker.remove(node)
            traversed_marker.append(node)
            tree.sync()
            for child in node.children:
                frontier.append(child)
                frontier_marker.append(child)
            tree.sync()

    def run(self, tree):
        with tree.postpone_sync():
            super().run(tree)
        traversed_marker = tree.create_multi_marker("Traversed")
        frontier_marker = tree.create_multi_marker("Frontier")
        tree.stats.traversed_nodes = 0
        self.traverse(tree, tree.root, traversed_marker, frontier_marker)
