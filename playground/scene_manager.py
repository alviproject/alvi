import importlib
import multiprocessing

from playground import settings


def load_default_scenes():
    for scene in settings.default_scenes:
        module_name, class_name = scene.rsplit(".", 1)
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        process = multiprocessing.Process(target=class_.start)
        process.start()