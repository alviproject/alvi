import importlib
import multiprocessing
import tornado.options


tornado.options.define("default_scenes", help="list of auto-loaded scenes", multiple=True)


def load_default_scenes():
    for scene in tornado.options.options.default_scenes:
        module_name, class_name = scene.rsplit(".", 1)
        module = importlib.import_module(module_name)
        class_ = getattr(module, class_name)
        process = multiprocessing.Process(target=class_.start)
        process.start()