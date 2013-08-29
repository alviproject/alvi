import inspect

from django.shortcuts import render
from multiprocessing import Process
from multiprocessing import Queue
from django.template import RequestContext

from . import connections
from . import scenes
import __main__


def home(request):
    source = inspect.getsource(__main__)

    context = RequestContext(request, {
        'source': source,
    })
    return render(request, 'home.html', context_instance=context)


def run(request, id):
    scene = scenes.scenes[int(id)]
    queue = Queue()
    name, run, Space, source = scene
    process = Process(target=run, args=(queue, ))
    process.start()
    connections.queues[process.pid] = queue

    context = RequestContext(request, {
        'session_id': process.pid,
        'name': name,
        'source': source
    })
    return render(request, Space.template, context_instance=context)
