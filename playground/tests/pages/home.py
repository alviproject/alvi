from selenium.webdriver.common.by import By
from . import base


class Home(base.Page):
    scene_links = base.make_elements(By.CSS_SELECTOR, "ul.scenes li a")

