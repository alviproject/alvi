import alvi.client.api
import alvi.client.api.tree as tree
import alvi.client.containers


class TreeCreateNode(alvi.client.api.BaseScene):
    def run(self, pipe):
        tree.create_node(pipe, id=0, parent_id=0, value=1)
        tree.create_node(pipe, id=1, parent_id=0, value=2)
        tree.create_node(pipe, id=2, parent_id=0, value=3)
        tree.create_node(pipe, id=3, parent_id=1, value=4)
        pipe.sync()

    @classmethod
    def container_name(cls):
        return "Tree"


if __name__ == "__main__":
    TreeCreateNode.start()