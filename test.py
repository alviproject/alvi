from playground import service
from playground.scenes import Booble
from playground.scenes import BoobleCartesian
from playground.scenes import CreateTree
from playground.scenes import BinarySearchTree


N = 100  # number of points and max value of the point
service.register_scene(Booble(N))
service.register_scene(BoobleCartesian(N))
service.register_scene(CreateTree(N))
service.register_scene(BinarySearchTree(N))
service.run()
