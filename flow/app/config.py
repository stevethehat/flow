from pyramid.response import Response
import admin_handler

# example config
static_paths = [
	{ "url_prefix": "js", "local_path": "C:\\Development\\Personal\\flow\\static\\app\\js" },
	{ "url_prefix": "css", "local_path": "C:\\Development\\Personal\\flow\\static\\app\\css" },
	{ "url_prefix": "html", "local_path": "C:\\Development\\Personal\\flow\\static\\app\\html" },
]

def test_dynamic_handler(request):
	return(Response("hello this is a dynamic page"))

def nodes_handler(request):
	return(admin_handler.admin_handler(request))

dynamic_url_handlers = [
	{ "route": "/nodes/{action}/*subpath", "name": "nodes_handler", "view": nodes_handler}
]