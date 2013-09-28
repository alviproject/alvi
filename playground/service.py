import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "playground.settings")

import simplejson
import django.core.handlers.wsgi
from django.conf import settings
import tornado.options
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

from . import connections
from . import scenes
from . import scene_manager


def get_json_data(request):
    data = request.get_argument("data")
    return simplejson.loads(data)


class RegisterSceneHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        data = get_json_data(self)
        scenes.register(name=data['name'], container_name=data['container'], request=self)


class SyncSceneHandler(tornado.web.RequestHandler):
    #@tornado.web.asynchronous
    def post(self, *args, **kwargs):
        try:
            data = get_json_data(self)
            instance_id = data['instance_id']
            scene = scenes.scene_instances[instance_id]
            for message in data['messages']:
                scene.evaluate_message(message)
            self.write("{}")
        except Exception as x:
            print(x)
            raise x


def run():
    wsgi_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
    router = connections.sockjs.tornado.SockJSRouter(connections.Connection, '/rt')
    tornado_app = tornado.web.Application(
        router.urls +
        [
            (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(settings.BASE_DIR, 'data', 'static')}),
            ("/" + settings.API_URL_SCENE_REGISTER, RegisterSceneHandler),
            ("/" + settings.API_URL_SCENE_SYNC, SyncSceneHandler),
            ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(8000)
    scene_manager.load_default_scenes()
    tornado.ioloop.IOLoop.instance().start()


def register_scene(*args, **kwargs):
    scenes.register(*args, **kwargs)