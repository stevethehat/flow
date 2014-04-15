import imp
import flow.app.config as installation_config
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from flow.util.server_base import ServerBase

def page_server(request):
	response = "<h1>Test</h1><p>[%s]</p><p>[%s]</p>[%s]" % ("/".join(request.subpath), request.user_agent, str(request.registry))	
	return Response(response)

class App(ServerBase):
	pass

def app_start():
	print "starting app..."

	app = App(installation_config)
	app.start()

