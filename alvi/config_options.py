import tornado.options


tornado.options.define("port", help="server port", default=8000, type=int)
tornado.options.define("address", help="server address", default="127.0.0.1", type=str)
tornado.options.define("default_scenes", help="list of auto-loaded scenes", multiple=True)