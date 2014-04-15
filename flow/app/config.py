from pyramid.response import Response

# example config
static_paths = [
	{ "url_prefix": "js", "local_path": "C:\\Development\\Personal\\flow\\static\\app\\js" },
	{ "url_prefix": "css", "local_path": "C:\\Development\\Personal\\flow\\static\\app\\css" },
	{ "url_prefix": "html", "local_path": "C:\\Development\\Personal\\flow\\static\\app\\html" },
]

#def test_dynamic_handler(request):
#	return(Response("hello this is a dynamic page"))


dynamic_url_handlers = [
#	{ "route": "/dynamic/{url}", "name": "dynamic_test", "view": test_dynamic_handler}
]