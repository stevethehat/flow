import os
from pyramid.response import Response
import admin_handler

root_path = os.path.realpath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, os.pardir))

# example config
static_paths = [
	{ "url_prefix": "js", "local_path": os.path.join(root_path, "static", "app", "js") },
	{ "url_prefix": "css", "local_path": os.path.join(root_path, "static", "app", "css") },
	{ "url_prefix": "html", "local_path": os.path.join(root_path, "static", "app", "html") },	
	{ "url_prefix": "fonts", "local_path": os.path.join(root_path, "static", "app", "fonts") },	
	{ "url_prefix": "assets", "local_path": os.path.join(root_path, "static", "app", "assets") },
]

def test_dynamic_handler(request):
	return(Response("hello this is a dynamic page"))

def nodes_handler(request):
	return(admin_handler.admin_handler(request))

dynamic_url_handlers = [
	{ "route": "/nodes/{action}/*subpath", "name": "nodes_handler", "view": nodes_handler}
]