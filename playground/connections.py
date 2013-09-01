import logging
import sockjs.tornado
import simplejson
from tornado import gen
from tornado.ioloop import IOLoop
from sockjs.tornado import proto


logger = logging.getLogger(__name__)


class Connection(sockjs.tornado.SockJSConnection):
    def on_open(self, info):
        logger.info("new connection")

    def on_message(self, message):
        #TODO catch errors (queue does not exists, cannot parse, etc)
        #TODO check rights to access the queue
        message = simplejson.loads(message)
        session_id = message['session_id']
        session_id = int(session_id)
        logger.info("session_id=%d" % session_id)
        queue = queues[session_id]

        if message['message'] == 'init':
            def notify(fd, events):
                action = queue.get()
                self.send(proto.json_encode(action))
            IOLoop.instance().add_handler(queue._reader.fileno(), notify, IOLoop.READ)

    def on_close(self):
        logger.info("closing connection")
        #TODO kill the process


queues = {}
#scenes = [] #TODO