import logging
from alvi.tests.resources.base import Resource
from alvi.tests.resources.base import ResourceFactory
from selenium import webdriver

logger = logging.getLogger(__name__)


class Browser(ResourceFactory):
    @staticmethod
    def create():
        return LocalBrowser()


class LocalBrowser(Resource):
    def __init__(self):
        logger.info("setting up browser")
        #TODO config
        #self._driver = webdriver.Firefox()
        self._driver = webdriver.Chrome()
        #username = os.environ["SAUCE_USERNAME"]
        #access_key = os.environ["SAUCE_ACCESS_KEY"]
        #capabilities = {
        #    "tunnel-identifier": os.environ["TRAVIS_JOB_NUMBER"],
        #    "build": os.environ["TRAVIS_BUILD_NUMBER"],
        #    "tags": [os.environ["TRAVIS_PYTHON_VERSION"], "CI"],
        #}
        #hub_url = "%s:%s@localhost:4445" % (username, access_key)
        #cls._browser = webdriver.Remote(
        #    desired_capabilities=capabilities,
        #    command_executor="http://%s/wd/hub" % hub_url)

    def destroy(self):
        logger.info("terminating browser")
        #self.driver.quit()

    @property
    def driver(self):
        return self._driver