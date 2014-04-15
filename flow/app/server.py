from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def page_server(request):
	response = "<h1>Test</h1><p>[%s]</p><p>[%s]</p>[%s]" % ("/".join(request.subpath), request.user_agent, str(request.registry))	
	return Response(response)

def app_start():
	print "starting web app..."

	config = Configurator()
	#config.add_route("page_server", "")
	config.add_route("page_server", "/*subpath")
	config.add_view(page_server, route_name="page_server")

	app = config.make_wsgi_app()
	server = make_server("0.0.0.0", 8080, app)
	server.serve_forever()