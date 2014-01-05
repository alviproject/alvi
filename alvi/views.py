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


def run(request, name):
    scene_class = scenes.scene_classes[name]
    scene = scene_class.create()
    context = RequestContext(request, {
        'scene': scene,
    })

    #if request.method == "POST":
    #    form = scene.Form(request.POST)
    #    if form.is_valid():
    #        queue = Queue()
    #        process = Process(target=scene._run, args=(queue, form))
    #        process.start()
    #        connections.queues[process.pid] = queue
    #
    #        context['session_id'] = process.pid
    #        return render(request, scene.template(), context_instance=context)
    #else:
    #    form = scene.Form()
    #context['form'] = form
    return render(request, scene.template(), context_instance=context)


def run(request, name):
    scene_class = scenes.scene_classes[name]
    if request.method == "POST":
        options = dict(request.POST.items())
        del options['csrfmiddlewaretoken']
        scene = scene_class.create(options)
        context = RequestContext(request, {
            'scene': scene,
        })
        return render(request, scene.template(), context_instance=context)
    context = RequestContext(request, {
        'name': scene_class.name(),
        'form': scene_class.form(),
    })
    return render(request, "init_scene.html", context_instance=context)