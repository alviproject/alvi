from django.shortcuts import render
from multiprocessing import Process
from multiprocessing import Queue
from django.template import RequestContext
import connections


def run(request, id):
    scene = connections.scenes[int(id)]
    queue = Queue()
    process = Process(target=scene['algorithm'], args=(queue, ))
    process.start()
    connections.queues[process.pid] = queue

    context = RequestContext(request, {
        'session_id': process.pid,
    })
    return render(request, scene['space'].template, context_instance=context)
