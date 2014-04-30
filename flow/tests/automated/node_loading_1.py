from flow.app.hierarchy import Hierarchy
import shutil

def test_1(flow):
	flow.hierarchy.init()
	
	print "load root node..."
	root = flow.hierarchy.get_node(1)
	admin = flow.hierarchy.add_node("admin", "Administration", parent_node = root)

	print root
	print admin

	children = root.children()