import os, ast, shutil
from flowbase import FlowBase

class NodeStore_File(FlowBase):
	"""
	Basic NodeStore implementation based on filesystem.
	"""
	def __init__(self, env):
		self.env = env
		self.root_path = os.path.join(env.config["approot"], "nodes")

	def get_uid(self):
		uid_file_name = os.path.join(self.root_path, "uid")

		new_uid = 1
		if os.path.exists(uid_file_name):
			uid_file = open(uid_file_name, "r")
			new_uid = int(uid_file.read()) + 1
			uid_file.close()
			os.remove(uid_file_name)

		uid_file = open(uid_file_name, "w")
		uid_file.write(str(new_uid))
		uid_file.close()

		return(str(new_uid))

	def init(self):
		if os.path.exists(self.root_path):
			shutil.rmtree(self.root_path)
		os.makedirs(self.root_path)

	def get_node_directory_path(self, uid):
		node_directory_path = os.path.join(self.root_path, str(uid))
		return(node_directory_path)

	def get_node_data_path(self, uid):
		return(os.path.join(self.get_node_directory_path(uid), ".node"))

	def get(self, uid):
		result = None
		full_file_name = self.get_node_data_path(uid)
		if os.path.exists(full_file_name):
			result = self.load_object(full_file_name, None)
		return(result)

	def add(self, data):
		uid = uid = self.get_uid()
		node_directory_path = self.get_node_directory_path(uid)
		if not(os.path.exists(node_directory_path)):
			os.makedirs(node_directory_path)

		self.update(uid, data)
		return(uid)

	def update(self, uid, data):
		full_file_name = self.get_node_data_path(uid)
		self.save_object(full_file_name, data)

	def delete(self, uid):
		pass

	def children(self, uid):
		print "load children of '%s'" % uid
		node = self.load_object(str(uid), None)
		print "node = %s" % node
		print "children = %s" % node["child_uids"] 
		results = []
		if node != None:
			for child_node_uid in node["child_uids"]: 
				print "add child"
				results.append(self.load_object(child_node_uid, None))
		return(results)
