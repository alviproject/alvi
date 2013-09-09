import random


class LinearSearch(object):
    def __init__(self, n):
        self.n = n

    def run(self, list):
        wanted_id = random.randint(0, self.n)
        head = list.create_node(random.randint(1, self.n))
        node = head
        for i in range(self.n-1):
            value = random.randint(1, self.n)
            node.next = list.create_node(value)
            node = node.next

            if node.id == wanted_id:
                list.create_marker("wanted", node)
        list.sync()

        seeker = list.create_marker("seeker", head)
        list.sync()
        node = head.next
        while node:
            seeker.move(node)
            list.sync()
            if wanted_id == node.id: #TODO nodes shall support comparison
                break
            node = node.next
        list.sync()