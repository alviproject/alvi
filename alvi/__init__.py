from . import scenes


def context_processor(request):
    return {
        'scene_classes': scenes.scene_classes,
    }