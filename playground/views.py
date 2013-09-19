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
    context = RequestContext(request, {
        'scene': scene,
        'scene_id': id,
    })

    if request.method == "POST":
        form = scene.Form(request.POST)
        if form.is_valid():
            queue = Queue()
            process = Process(target=scene._run, args=(queue, form))
            process.start()
            connections.queues[process.pid] = queue

            context['session_id'] = process.pid
            return render(request, scene.template(), context_instance=context)
    else:
        form = scene.Form()
    context['form'] = form
    return render(request, "init_scene.html", context_instance=context)
