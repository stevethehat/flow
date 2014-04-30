from nodestore_file import NodeStore_File

class Node:
	def __init__(self, hierarchy, uid, data = None):
		self.hierarchy = hierarchy
		self.uid = uid
		if data != None:
			self.data = data
		else:
			self.data = self.hierarchy.store.get(uid)

	def update(self):
		self.hierarchy.store.update(self.uid, self.data)

	def add_child(self, nodetype, description):
		
		data = { "nodetype": nodetype, "description": description, "child_uids": []}
		uid = self.hierarchy.store.add(data)

		self.data["child_uids"].append(uid)
		self.update()

		print "child uids '%s'" % self.data["child_uids"]

		return(self.hierarchy.get_node(uid))

	def children(self):
		children = self.hierarchy.store.children(self.uid)
		print children

	def edit(self):
		return("the result of the edit...")

	def __repr__(self):
		return("\n%s" % {"uid": self.uid, "data": self.data})
