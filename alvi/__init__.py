from . import scenes


def context_processor(request):
    return {
        'scenes': [(key, value.is_default()) for (key, value) in scenes.scene_classes.items()],
    }