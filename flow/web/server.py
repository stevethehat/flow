import imp
import flow.web.config as installation_config
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from flow.util.server_base import ServerBase

def page_server(request):
	response = "<h1>Test</h1><p>[%s]</p><p>[%s]</p>[%s]" % ("/".join(request.subpath), request.user_agent, str(request.registry))	
	return Response(response)

class WebApp(ServerBase):
	pass

def web_app_start():
	print "starting web app..."

	web_app = WebApp(installation_config)
	web_app.start()

