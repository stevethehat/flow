from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def page_server(request):
	return Response("response - " % dir(request.matchdict))

def app_start(arg1):
	print "starting web app..."

config = Configurator()
config.add_route("page_server", "")
config.add_view(page_server, route_name="page_server")

app = config.make_wsgi_app()
server = make_server("0.0.0.0", 8080, app)
server.serve_forever()