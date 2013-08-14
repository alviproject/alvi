class Node(object):
    _nodes = []  # take a note, that there will be separate _nodes array per every subclass

    def __init__(self):
        Node._nodes.append(self)
        self.id = len(Node._nodes) - 1