import sockjs.tornado
import simplejson
from tornado import gen
from tornado.ioloop import IOLoop
from sockjs.tornado import proto
from twiggy import log

sockjs_log = log.name("sockjs")


class Connection(sockjs.tornado.SockJSConnection):
    def on_open(self, info):
        sockjs_log.info("new connection")

    def on_message(self, message):
        #TODO catch errorrs (queue does not exists, cannot parse, etc)
        #TODO check rights to access the queue
        session_id = simplejson.loads(message)['session_id']
        session_id = int(session_id)
        sockjs_log.fields(session_id=session_id).info()
        queue = queues[session_id]

        def notify(fd, events):
            action = queue.get()
            self.send(proto.json_encode(action))

        IOLoop.instance().add_handler(queue._reader.fileno(), notify, IOLoop.READ)

    def on_close(self):
        sockjs_log.info("closing connection")
        #TODO kill the process


queues = {}
#scenes = [] #TODO