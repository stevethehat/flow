import os

class Hierarchy():
	def __init__(self):
		self.root_path = "/Users/stevethehat/Development/flow/nodes"
		pass

	def get_node(self, uid):
		full_path = self.root_path
		for uid_bit in uid.split("/"):
			full_path = os.path.join(full_path, uid_bit)

		full_path = os.path.join(full_path, ".node")
		print full_path

	def add_node(self, parent_uid, nodetype):
		pass