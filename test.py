from playground import service
from playground.scenes import Booble
from playground.scenes import CreateTree
from playground.scenes import BinarySearchTree
from playground.scenes import LinearSearch
from playground.scenes import BinarySearch
from playground.containers import List
from playground.containers import Array
from playground.containers import Tree
from playground.containers import BinaryTree


N = 256  # number of nodes and max value of the node
service.register_scene("Booble", Booble(N).run, Array)
service.register_scene("Create Tree", CreateTree(N).run, Tree)
service.register_scene("Binary Search Tree", BinarySearchTree(N).run, BinaryTree)
service.register_scene("Linear Search", LinearSearch(N).run, List)
service.register_scene("Binary Search", BinarySearch(N).run, Array)
service.run()
