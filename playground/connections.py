import logging
import sockjs.tornado
import simplejson
from tornado.ioloop import IOLoop
from sockjs.tornado import proto

import playground.scenes


logger = logging.getLogger(__name__)


class Connection(sockjs.tornado.SockJSConnection):
    def on_open(self, info):
        logger.info("new connection")

    def on_message(self, message):
        #TODO catch errors (queue does not exists, cannot parse, etc)
        #TODO check rights to access the queue
        message = simplejson.loads(message)
        scene_id = message['scene_id']
        logger.info("scene_id=%s" % scene_id)
        scene = playground.scenes.scene_instances[scene_id]

        if message['message'] == 'init':
            def notify(action):
                self.send(proto.json_encode([action]))  # TODO consider sending all actions at once
            scene.run(notify)
            #IOLoop.instance().add_handler(queue._reader.fileno(), notify, IOLoop.READ)

    def on_close(self):
        logger.info("closing connection")
        #TODO kill the process


#queues = {}
#scenes = [] #TODO