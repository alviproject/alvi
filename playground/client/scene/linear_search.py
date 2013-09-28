import random
import multiprocessing

from django.conf import settings

import playground.client.containers.list
import playground.client.utils


class LinearSearch:
    def generate_nodes(self, list, n):
        if n == 0:
            return
        list.create_head(random.randint(1, n))
        node = list.head
        for i in range(n-1):
            value = random.randint(1, n)
            node = node.create_child(value)
        list.sync()

    def search(self, list, wanted_value):
        #seeker = list.create_marker("seeker", list.head)
        list.sync()

        node = list.head
        while node:
            #seeker.move(node)
            list.sync()
            if wanted_value == node.value:
                #list.stats.found_id = node.id
                break
            node = node.next
        else:
            list.stats.not_found = ""
        list.sync()

    def run(self, scene_instance_id):
        print("ok")
        n = 8
        list = playground.client.containers.List(scene_instance_id)
        wanted_value = random.randint(0, n)
        list.stats.wanted_value = wanted_value

        self.generate_nodes(list, n)
        self.search(list, wanted_value)

        #TODO
        node = list.head
        print(node)
        while node:
            node.value = 3
            node = node.next
        list.sync()


def run():
    scene = LinearSearch()

    while True:
        post_data = {
            'name': 'LinearSearch'
        }
        response = playground.client.utils.post_to_server(settings.API_URL_SCENE_REGISTER, post_data)
        scene_instance_id = response['scene_instance_id']
        process = multiprocessing.Process(target=scene.run, args=(scene_instance_id,))
        process.start()
