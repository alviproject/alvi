from . import scenes


def context_processor(request):
    scene_names = [name for name, _, _, _ in scenes.scenes]
    return {
        'scene_names': scene_names,
    }