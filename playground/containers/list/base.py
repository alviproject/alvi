import abc
from .. import base


class Node(base.Node):
    #TODO next, prev, etc, restrict interface? (getitem, setitem)
    pass


class List(base.Container):
    #head?
    @abc.abstractmethod
    def create_node(self, value):pass