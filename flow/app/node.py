from decorators import *
from nodestore_file import NodeStore_File
from flowbase import FlowBase

class Node(FlowBase):
	def __init__(self, flow, uid, data = None):
		super(Node, self).__init__(flow)
		self.hierarchy = self.flow.hierarchy
		self.uid = uid
		if data != None:
			self.data = data
		else:
			self.data = self.hierarchy.store.get(uid)

		self.nodetype = self.data["nodetype"]

	@cacheprop
	def definition(self):
		print "loading nodetype"
		return(self.flow.nodetypes.definitions[self.nodetype])

	def edit(self):
		return("the result of the edit...")

	def update(self):
		self.hierarchy.store.update(self.uid, self.data)

	def add_child(self, nodetype, description):
		data = { "parent_uid": self.uid, "nodetype": nodetype, "description": description, "child_uids": []}
		uid = self.hierarchy.store.add(data)

		self.data["child_uids"].append(uid)
		self.update()

		return(self.hierarchy.get_node(uid))

	def children(self):
		children = []
		for child_node_uid in self.data["child_uids"]:
			children.append(self.hierarchy.get_node(child_node_uid))
		return(children)

	def __repr__(self):
		return("\n%s" % {"uid": self.uid, "data": self.data})
