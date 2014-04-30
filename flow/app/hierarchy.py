import os
from nodestore_file import NodeStore_File
from node import Node

class Hierarchy():
	def __init__(self, env):
		self.env = env
		env.log("init Hierarchy")
		self.store = NodeStore_File(self.env)

	def get_node(self, uid):
		node = Node(self, uid)
		return(node)

	def add_node(self, uid, nodetype, parent_node = None, parent_uid = None, ):
		full_uid = None
		if parent_node != None:
			full_uid = "%s/%s" % (parent_node.uid, uid)
		if parent_uid != None:
			full_uid = "%s/%s" % (parent_uid, uid)

		data = {
			"nodetype": nodetype, "uid": full_uid
		}
		result = None
		if full_uid != None:
			self.store.add(full_uid, data)
			result = self.get_node(full_uid)

		return(result)
