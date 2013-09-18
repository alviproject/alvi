from playground import service
import playground.scenes
import playground.containers
import random


N = 1024


def sample_scene1(array):
    """example scene, create N random elements and iterate through each of them"""
    array.init(N)
    for i in range(N):
        array[i] = random.randint(0, N)
    array.sync()
    marker = array.create_marker("marker", 0)
    for i in range(1, array.size()):
        marker.move(i)
        array.sync()


class SampleScene_2(playground.scenes.Scene):
    """shows how to create class based scene"""
    def __init__(self, n):
        self.n = n

    def run(self, list):
        head = list.create_head(random.randint(0, self.n))
        node = head
        for i in range(self.n-1):
            node = node.create_child(random.randint(0, self.n))
        list.sync()
        node = head
        marker = list.create_marker("marker", node)
        for i in range(1, self.n):
            node = node.next
            marker.move(node)
            list.sync()

    def container_class(self):
        return playground.containers.List


service.register_scene(playground.scenes.make_scene("Sample Scene 1", sample_scene1, playground.containers.Array))
service.register_scene(SampleScene_2(N))
service.register_scene(playground.scenes.Booble(N))
service.register_scene(playground.scenes.SelectionSort(N))
service.register_scene(playground.scenes.InsertionSort(N))
service.register_scene(playground.scenes.ShellSort(N))
service.register_scene(playground.scenes.MergeSort(N))
service.register_scene(playground.scenes.CreateTree(N))
service.register_scene(playground.scenes.BinarySearchTree(N))
service.register_scene(playground.scenes.LinearSearch(N))
service.register_scene(playground.scenes.BinarySearch(N))
service.register_scene(playground.scenes.CreateGraph(N))
service.run()
