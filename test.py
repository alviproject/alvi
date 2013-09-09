from playground import service
#from playground.scenes import Booble
#from playground.scenes import BoobleCartesian
#from playground.scenes import CreateTree
#from playground.scenes import BinarySearchTree
from playground.scenes import LinearSearch
from playground.containers import List


N = 64  # number of points and max value of the point
#service.register_scene("Booble", Booble(N).run, Booble.Space)
#service.register_scene("Booble Cartesian", BoobleCartesian(N).run, BoobleCartesian.Space)
#service.register_scene("Create Tree", CreateTree(N).run, CreateTree.Space)
#service.register_scene("Binary Search Tree", BinarySearchTree(N).run, BinarySearchTree.Space)
service.register_scene("Linear Search", LinearSearch(N).run, List)
service.run()
