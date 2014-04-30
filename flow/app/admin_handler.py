from pyramid.response import Response
from flow import Flow

def admin_handler(request):
	flow = Flow(
		{
			"approot": "C:\\Development\\Personal\\flow"
		}
	)
	uid = "/".join(request.subpath)
	action = request.matchdict["action"]
	node = flow.hierarchy.get_node(uid)

	print node

	action_response = getattr(node, action, ["1234", "11"])()
	response = """
		<h1>node test response</h1>
		<p>uid = '%s'</p>
		<p>action = '%s'</p>
		<p>result = '%s'</p>
	""" % (uid, action, action_response)
	return(Response(response))


