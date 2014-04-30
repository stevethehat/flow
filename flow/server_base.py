import imp
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

def page_server(request):
	response = """
	<h1>/admin</h1>
	<p>[%s]</p>
	<p>[%s]</p>
	<p>[%s]</p>""" % ("/".join(request.subpath), request.user_agent, str(request.registry))	
	
	return Response(response)

class ServerBase:
	def __init__(self, installation_config):
		"""
		initialize Configurator and setup required routes
		"""
		self._app_config = Configurator()
		self._installation_config = installation_config

		# setup routes
		self.init_static_routes()
		self.init_modules()
		self.init_dynamic_routes()
		
		self.init_default_routes()

	def init_default_routes(self):
		self._app_config.add_route("page_server", "/*subpath")
		self._app_config.add_view(page_server, route_name="page_server")

	def init_static_routes(self):
		if self._installation_config.static_paths:
			for static_path in self._installation_config.static_paths:
				print "adding static path '/%s' > '%s'" % (static_path["url_prefix"], static_path["local_path"])
				self._app_config.add_static_view(name=static_path["url_prefix"], path=static_path["local_path"])

	def init_dynamic_routes(self):
		if self._installation_config.dynamic_url_handlers:
			for dynamic_url_handler in self._installation_config.dynamic_url_handlers:
				print "adding dynamic url handler '%s'" % (dynamic_url_handler["route"])

				self._app_config.add_route(dynamic_url_handler["name"], dynamic_url_handler["route"])
				self._app_config.add_view(dynamic_url_handler["view"], route_name=dynamic_url_handler["name"])				

	def init_modules(self):
		#module = imp.load_source("test_module", "C:\\Development\\Personal\\flow\\modules\\test_module.py")
		#module.init_web(self._app_config)
		pass

	def start(self):
		self.app = self._app_config.make_wsgi_app()
		self.server = make_server("0.0.0.0", 8080, self.app)
		self.server.serve_forever()		


def app_start():
	print "starting web app..."

	app = App()
	app.start()

