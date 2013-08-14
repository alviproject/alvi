import connections


def context_processor(request):
    return {
        'scenes': connections.scenes,
    }