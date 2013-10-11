import random

import alvi.client.containers
import alvi.client.utils
from . import base


class LinearSearch(base.Scene):
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
        found_index = 0
        while node:
            found_index += 1
            seeker.move(node)
            list.sync()
            if wanted_value == node.value:
                list.stats.found_index = found_index
                break
            node = node.next
        else:
            list.stats.not_found = ""
        list.sync()

    def run(self, list):
        n = 8
        wanted_value = random.randint(0, n)
        list.stats.wanted_value = wanted_value

        self.generate_nodes(list, n)
        self.search(list, wanted_value)

    @staticmethod
    def container_class():
        return alvi.client.containers.List


if __name__ == "__main__":
    LinearSearch.start()