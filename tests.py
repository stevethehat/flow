import os
from flow.app.flow import Flow
from flow.tests.automated.node_loading_1 import *

flow = Flow(
	{
		"approot": os.path.dirname(os.path.realpath(__file__))
	}
)

os.system("clear")
test_1(flow)