import os, ast

class FlowBase(object):
	def __init__(self, flow):
		self.flow = flow
		self.env = flow.env
		self.config = flow.env.config

	def load_object(self, full_file_name, default):
		result = default
		if os.path.exists(full_file_name):
			object_file = open(full_file_name, "r")
			result = ast.literal_eval(object_file.read())
			object_file.close()
		return(result)

	def save_object(self, full_file_name, obj):
		if os.path.exists(full_file_name):
			os.remove(full_file_name)

		object_file = open(full_file_name, "w")
		object_file.write(str(obj))
		object_file.close()