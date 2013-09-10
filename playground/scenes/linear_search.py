import random


class LinearSearch(object):
    def __init__(self, n):
        self.n = n

    def generate_nodes(self, list):
        if self.n == 0:
            return
        list.head = list.create_node(random.randint(1, self.n))
        node = list.head
        for i in range(self.n-1):
            value = random.randint(1, self.n)
            node.next = list.create_node(value)
            node = node.next
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

    def run(self, list):
        wanted_value = random.randint(0, self.n)
        list.stats.wanted_value = wanted_value

        self.generate_nodes(list)
        self.search(list, wanted_value)

