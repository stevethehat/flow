from flow.app.hierarchy import Hierarchy

def test_1(flow):
	print "load root node..."
	root = flow.hierarchy.get_node("root")
	print root

	admin = flow.hierarchy.add_node("admin", "admin", parent_node = root)
	print admin