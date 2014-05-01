from flow.app.hierarchy import Hierarchy
import shutil

def test_1(flow):
	flow.hierarchy.init()
	
	print "load root node..."
	root = flow.hierarchy.get_node(1)
	print "add admin node..."
	print ""

	admin = flow.hierarchy.add_node("admin", "Administration", parent_node = root)
	websites = flow.hierarchy.add_node("websites", "Websites", parent_node = root)
	website = flow.hierarchy.add_node("website", "Steves Website", parent_node = websites)

	print "root = '%s'\n" % root
	print "admin = '%s'\n" % admin
	print "websites = '%s'\n" % websites

	children = root.children()
	print "children = '%s'\n" % children