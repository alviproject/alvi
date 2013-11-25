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
        #TODO get url from backend resource
        self._root.get("http://%s:%d" % (options.address, options.port))


def get_driver_from_element(element):
    try:
        return get_driver_from_element(element.parent)
    except AttributeError:
        #if it has no parent it has to be a driver
        return element