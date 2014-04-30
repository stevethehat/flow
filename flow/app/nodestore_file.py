import os, ast

class NodeStore_File():
	"""
	Basic NodeStore implementation based on filesystem.
	"""
	def __init__(self):
		#self.root_path = "/Users/stevethehat/Development/flow/nodes"		
		self.root_path = "C:\\Development\\Personal\\flow\\nodes"

	def get_node_directory_path(self, uid):
		node_directory_path = self.root_path
		for uid_bit in uid.split("/"):
			node_directory_path = os.path.join(node_directory_path, uid_bit)
		return(node_directory_path)

	def get_node_data_path(self, uid):
		return(os.path.join(self.get_node_directory_path(uid), ".node"))

	def get(self, uid):
		result = None
		full_file_name = self.get_node_data_path(uid)
		if os.path.exists(full_file_name):
			object_file = open(full_file_name, "r")
			result = ast.literal_eval(object_file.read())
			object_file.close()
		return(result)

	def add(self, uid, data):
		node_directory_path = self.get_node_directory_path(uid)
		if not(os.path.exists(node_directory_path)):
			os.makedirs(node_directory_path)

		full_file_name = self.get_node_data_path(uid)
		object_file = open(full_file_name, "w")
		object_file.write(str(data))
		object_file.close()



	def update(self, uid, data):
		pass

	def delete(self, uid):
		pass

	def children(self, uid):
		pass
