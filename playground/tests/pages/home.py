from selenium.webdriver.common.by import By
from tornado.options import options


def make_elements(by, value):
    def foo(self):
        return self._driver.find_elements(by, value)
    return property(foo)


class Home:
    def __init__(self, driver):
        self._driver = driver

    def load(self):
        self._driver.get("http://%s:%d" % (options.address, options.port))

    @property
    def title(self):
        return self._driver.title

    scene_links = make_elements(By.CSS_SELECTOR, "ul.scenes li a")