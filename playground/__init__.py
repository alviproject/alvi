import scenes


def context_processor(request):
    return {
        'scenes': scenes.scenes,
    }