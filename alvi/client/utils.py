import urllib.parse
import tornado.httpclient
import json
from tornado.options import options
#TODO don't use server options
import alvi.config_options


def post_to_server(path, data):
    http_client = tornado.httpclient.HTTPClient()
    json_data = dict(data=json.dumps(data))
    body = urllib.parse.urlencode(json_data)
    url = "http://%s:%d/%s" % (options.address, options.port, path)
    response = http_client.fetch(url, method='POST', body=body, request_timeout=0)
    return json.loads(response.body.decode("utf-8"))