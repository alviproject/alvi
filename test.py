from playground import service
from playground.scenes import Booble
from playground.scenes import CreateTree
#from playground.scenes import BinarySearchTree
from playground.scenes import LinearSearch
from playground.containers import List
from playground.containers import Array
from playground.containers import Tree


N = 4  # number of nodes and max value of the node
service.register_scene("Booble", Booble(N).run, Array)
service.register_scene("Create Tree", CreateTree(N).run, Tree)
#service.register_scene("Binary Search Tree", BinarySearchTree(N).run, BinarySearchTree.Space)
service.register_scene("Linear Search", LinearSearch(N).run, List)
service.run()
