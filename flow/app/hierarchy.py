import os
from nodestore_file import NodeStore_File
from node import Node

class Hierarchy():
	def __init__(self):
		self.store = NodeStore_File()

	def get_node(self, uid):
		print "Hierarchy.get_node '%s'" % uid
		node = Node(self, uid)
		print node
		return(node)

	def add_node(self, parent_uid, nodetype):
		data = {
			"nodetype": nodetype, "parent_uid": parent_uid, "uid": ""
		}
		return(self.get_node(uid))
