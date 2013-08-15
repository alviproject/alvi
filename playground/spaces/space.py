class Stats(object):
    def __init__(self, queue):
        object.__setattr__(self, 'queue', queue)

    def __setattr__(self, name, value):
        self.queue.put(dict(
            type='update_stats',
            name=name,
            value=value,
        ))
        return object.__setattr__(self, name, value)


class Space(object):
    """abstract space, not to be used directly"""

    def __init__(self, queue):
        self.queue = queue
        self.stats = Stats(queue)