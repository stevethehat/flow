def test_dynamic_loaded_handler(request):
	return(Response("hello this is a dynamic loaded page"))

def setup_web_routes(config):
	print "setup test module routes..."
	config.add_route("dynamicloadtest1", "/dynamicload{url}")
	config.add_view(test_dynamic_loaded_handler, route_name="dynamicloadtest1")				


def init_web(config):
	print "init test module...."
	config.include(setup_web_routes)