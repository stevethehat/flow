import os
from nodestore_file import NodeStore_File
from node import Node

class Hierarchy():
	def __init__(self, env):
		self.env = env
		env.log("init Hierarchy")
		self.store = NodeStore_File(self.env)

	def init(self):
		self.store.init()
		self.store.add({ "nodetype": "root", "description": "Flow Root", "child_uids": []})

	def get_node(self, uid):
		node = Node(self, uid)
		return(node)

	def add_node(self, nodetype, description, parent_node = None, parent_uid = None):
		if parent_node == None:
			parent_node = self.get_node(parent_uid)

		result = parent_node.add_child(nodetype, description)
		return(result)
