from playground import service
import playground.scenes
import playground.containers
import random


def sample_scene_1(array, form_data):
    """example scene, create N random elements and iterate through each of them"""
    n = form_data['n']
    array.init(n)
    for i in range(n):
        array[i] = random.randint(0, n)
    array.sync()
    marker = array.create_marker("marker", 0)
    for i in range(1, array.size()):
        marker.move(i)
        array.sync()


class SampleScene_2(playground.scenes.Scene):
    """shows how to create class based scene"""
    Container = playground.containers.List

    def run(self, list, form_data):
        n = form_data['n']
        head = list.create_head(random.randint(0, n))
        node = head
        for i in range(n-1):
            node = node.create_child(random.randint(0, n))
        list.sync()
        node = head
        marker = list.create_marker("marker", node)
        for i in range(1, n):
            node = node.next
            marker.move(node)
            list.sync()


service.register_scene(playground.scenes.make_scene("Sample Scene 1", sample_scene_1, playground.containers.Array))
service.register_scene(SampleScene_2())
service.register_scene(playground.scenes.Booble())
service.register_scene(playground.scenes.SelectionSort())
service.register_scene(playground.scenes.InsertionSort())
service.register_scene(playground.scenes.ShellSort())
service.register_scene(playground.scenes.MergeSort())
service.register_scene(playground.scenes.CreateTree())
service.register_scene(playground.scenes.BinarySearchTree())
service.register_scene(playground.scenes.LinearSearch())
service.register_scene(playground.scenes.BinarySearch())
service.register_scene(playground.scenes.CreateGraph())
service.run()
