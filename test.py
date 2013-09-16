from playground import service
from playground.scenes import Booble
from playground.scenes import CreateTree
from playground.scenes import BinarySearchTree
from playground.scenes import LinearSearch
from playground.scenes import BinarySearch
from playground.scenes import CreateGraph
from playground.scenes import SelectionSort
from playground.scenes import InsertionSort
from playground.scenes import ShellSort
from playground.scenes import MergeSort

from playground.containers import List
from playground.containers import Array
from playground.containers import Tree
from playground.containers import BinaryTree
from playground.containers import Graph


N = 1024  # number of nodes and max value of the node
service.register_scene("Booble", Booble(N).run, Array)
service.register_scene("Selection Sort", SelectionSort(N).run, Array)
service.register_scene("Insertion Sort", InsertionSort(N).run, Array)
service.register_scene("Shell Sort", ShellSort(N).run, Array)
service.register_scene("Merge Sort", MergeSort(N).run, Array)
service.register_scene("Create Tree", CreateTree(N).run, Tree)
service.register_scene("Binary Search Tree", BinarySearchTree(N).run, BinaryTree)
service.register_scene("Linear Search", LinearSearch(N).run, List)
service.register_scene("Binary Search", BinarySearch(N).run, Array)
service.register_scene("Create Graph", CreateGraph(N).run, Graph)
service.run()
