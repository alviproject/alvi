import os
import logging
import alvi.config
alvi.config.configure()

import json
import django.core.handlers.wsgi
from django.conf import settings
import tornado.options
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi

from alvi import connections
from alvi import scenes
from alvi import scene_manager

API_URL_SCENE_REGISTER = 'api/scene/register'
API_URL_SCENE_SYNC = 'api/scene/sync'

logger = logging.getLogger(__name__)


def get_json_data(request):
    data = request.get_argument("data")
    return json.loads(data)


class RegisterSceneHandler(tornado.web.RequestHandler):
    @tornado.web.asynchronous
    def post(self, *args, **kwargs):
        data = get_json_data(self)
        scenes.register(data=data, request=self)


class SyncSceneHandler(tornado.web.RequestHandler):
    #@tornado.web.asynchronous
    def post(self, *args, **kwargs):
        #try:
            data = get_json_data(self)
            instance_id = data['instance_id']
            scene = scenes.scene_instances[instance_id]
            for message in data['messages']:
                scene.evaluate_message(message)
            self.write("{}")
        #except Exception as x:
        #    print(x)
        #    raise x


def run():
    wsgi_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
    router = connections.sockjs.tornado.SockJSRouter(
        connections.Connection,
        '/rt',
        dict(disabled_transports=['websocket'])
    )
    tornado_app = tornado.web.Application(
        router.urls +
        [
            (r"/static/(.*)", tornado.web.StaticFileHandler, {"path": os.path.join(settings.PROJECT_BASE_DIR, 'static')}),
            ("/" + API_URL_SCENE_REGISTER, RegisterSceneHandler),
            ("/" + API_URL_SCENE_SYNC, SyncSceneHandler),
            ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
        ])
    server = tornado.httpserver.HTTPServer(tornado_app)
    server.listen(tornado.options.options.port, tornado.options.options.address)
    scene_manager.load_default_scenes()
    logger.info("listening at: http://%s:%s", tornado.options.options.address, tornado.options.options.port)
    tornado.ioloop.IOLoop.instance().start()


def register_scene(*args, **kwargs):
    scenes.register(*args, **kwargs)


if __name__ == "__main__":
    run()
