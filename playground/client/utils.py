import urllib.parse
import tornado.httpclient
import simplejson
from django.conf import settings


def post_to_server(path, data):
    http_client = tornado.httpclient.HTTPClient()
    json_data = dict(data=simplejson.dumps(data))
    body = urllib.parse.urlencode(json_data)
    url = "http://%s:%d/%s" % (settings.HOST, settings.PORT, path)
    response = http_client.fetch(url, method='POST', body=body, request_timeout=0)
    return simplejson.loads(response.body.decode("utf-8"))