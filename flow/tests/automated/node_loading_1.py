from flow.app.hierarchy import Hierarchy

def test_1():
	print "load hierarchy..."
	h = Hierarchy()
	print "load root node..."
	r = h.get_node("/root")
	print "root"