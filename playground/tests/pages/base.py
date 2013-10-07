from tornado.options import options


def make_elements(by, value):
    def wrapper(self):
        return self._root.find_elements(by, value)
    return property(wrapper)


def make_element(by, value):
    def wrapper(self):
        return self._root.find_element(by, value)
    return property(wrapper)


class Page:
    def __init__(self, root):
        self._root = root

    @property
    def title(self):
        return self._root.title

    def goto(self):
        """get to the page by loading home page and clicking through subpages"""
        self._root.get("http://%s:%d" % (options.address, options.port))