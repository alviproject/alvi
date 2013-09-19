import random

from . import base
import playground.containers


class LinearSearch(base.Scene):
    Container = playground.containers.List

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
        seeker = list.create_marker("seeker", list.head)
        list.sync()

        node = list.head
        while node:
            seeker.move(node)
            list.sync()
            if wanted_value == node.value:
                list.stats.found_id = node.id
                break
            node = node.next
        else:
            list.stats.not_found = ""
        list.sync()

    def run(self, list, form_data):
        n = form_data['n']
        wanted_value = random.randint(0, n)
        list.stats.wanted_value = wanted_value

        self.generate_nodes(list, n)
        self.search(list, wanted_value)