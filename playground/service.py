import twiggy
twiggy.quickSetup()

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "playground.settings")

import django.core.handlers.wsgi
from django.conf import settings
import tornado.options
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import connections


def run():
    wsgi_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
    router = connections.sockjs.tornado.SockJSRouter(connections.Connection, '/rt')
    tornado_app = tornado.web.Application(
        router.urls +
        [
            (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(settings.BASE_DIR, 'data', 'static')}),
            ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(8000)
    tornado.ioloop.IOLoop.instance().start()


def add_scene(name, algorithm, space):
    space = {'name': name, 'algorithm': algorithm, 'space': space}
    connections.scenes.append(space)
