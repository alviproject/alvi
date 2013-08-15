class register(object):
    def __init__(self, Space):
        self.Space = Space

    def _run(self, queue):
        obj = self.cls()
        obj.space = self.Space(queue)
        return obj.run(queue)

    def __call__(self, cls):
        def name(self):
            return self.__class__.__name__

        self.cls = cls
        scenes.append(cls)
        cls._run = self._run
        cls.Space = self.Space
        cls.name = name
        return cls


scenes = []