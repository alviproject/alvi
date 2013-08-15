from django.shortcuts import render
from multiprocessing import Process
from multiprocessing import Queue
from django.template import RequestContext
import connections
import scenes


def run(request, id):
    scene = scenes.scenes[int(id)]
    queue = Queue()
    process = Process(target=scene._run, args=(queue, ))
    process.start()
    connections.queues[process.pid] = queue

    context = RequestContext(request, {
        'session_id': process.pid,
    })
    return render(request, scene.Space.template, context_instance=context)
