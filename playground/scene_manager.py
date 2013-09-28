import importlib
import multiprocessing

from playground import settings


def load_default_scenes():
    for scene in settings.default_scenes:
        scene_module = importlib.import_module(scene)
        process = multiprocessing.Process(target=scene_module.run)
        process.start()