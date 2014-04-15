from pyramid.response import Response

# example config
static_paths = [
	{ "url_prefix": "assets", "local_path": "C:\\Development\\Personal\\flow\\static\\frontend\\assets" },
	{ "url_prefix": "js", "local_path": "C:\\Development\\Personal\\flow\\static\\shared\\js" },
	{ "url_prefix": "css", "local_path": "C:\\Development\\Personal\\flow\\static\\shared\\css" },
]

def test_dynamic_handler(request):
	return(Response("hello this is a dynamic page"))


dynamic_url_handlers = [
	{ "route": "/dynamic/{url}", "name": "dynamic_test", "view": test_dynamic_handler}
]