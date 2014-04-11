import flow.web.config as installation_config
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def page_server(request):
	response = "<h1>Test</h1><p>[%s]</p><p>[%s]</p>[%s]" % ("/".join(request.subpath), request.user_agent, str(request.registry))	
	return Response(response)

class App:
	def __init__(self):
		"""
		initialize Configurator and setup required routes
		"""
		self._app_config = Configurator()
		self._installation_config = installation_config

		# setup routes
		self.init_static_routes()

		self.init_default_routes()

	def init_default_routes(self):
		self._app_config.add_route("page_server", "/*subpath")
		self._app_config.add_view(page_server, route_name="page_server")

	def init_static_routes(self):
		if installation_config.static_paths:
			for static_path in installation_config.static_paths:
				print "adding static path '/%s' > '%s'" % (static_path["url_prefix"], static_path["local_path"])
				self._app_config.add_static_view(name=static_path["url_prefix"], path=static_path["local_path"])


	def start(self):
		self.app = self._app_config.make_wsgi_app()
		self.server = make_server("0.0.0.0", 8080, self.app)
		self.server.serve_forever()		


def app_start():
	print "starting web app..."

	app = App()
	app.start()

