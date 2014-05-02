import os
from flow.app.flow import Flow
from flow.tests.automated.node_loading_1 import *

os.system("clear")
flow = Flow(
	{
		"approot": os.path.dirname(os.path.realpath(__file__))
	}
)

test_1(flow)