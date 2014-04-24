import os, ast, imp, sys
from decorators import BaseDecorator
"""
nodetypes
"""

sys.path.append("/Users/stevethehat/Development/flow")

def ast_loader(full_file_name, default):
	result = default
	if os.path.exists(full_file_name):
		object_file = open(full_file_name, "r")
		result = ast.literal_eval(object_file.read())
		object_file.close()
	return(result)

class NodeTypes:
	def __init__(self):
		print "init NodeTypes..."
		self.root_path = "/Users/stevethehat/Development/flow/modules"
		self.definitions = []

	def nodedefinition_processor(self, file_name):
		print "nodedefinition_processor %s" % file_name
		try:
			definition_file = open(file_name, "r")
			definition = ast.literal_eval(definition_file.read())
			definition_file.close()

			self.definitions.append(definition)
		except Exception, e: 
			print "Exception processing %s\n%s" % (file_name, e.message)

	def nodeclass_processor(self, file_name):
		print "nodeclass_processor %s" % file_name
		imp.load_source("page", file_name)

	def rebuild(self):
		print "rebuild nodetypes..."
		print "\n\nbuild nodedefs"
		self.walk_directories(".nodedef", self.nodedefinition_processor)
		print "\n\nbuild classes"

		full_file_name = os.path.join(self.root_path, "nodeclasses")
		if os.path.exists(full_file_name):
			os.remove(full_file_name)

		full_file_name = os.path.join(self.root_path, "nodeactions")
		if os.path.exists(full_file_name):
			os.remove(full_file_name)

		self.walk_directories(".py", self.nodeclass_processor)

	def output(self):
		print self.definitions
		print str(ast_loader(os.path.join(self.root_path, "nodeclasses"), []))
		print str(ast_loader(os.path.join(self.root_path, "nodeactions"), []))

	def walk_directory(self, path, file_type, processor):
		print "\n>> %s" % path
		ext = file_type[:len(file_type)]

		for file_name in os.listdir(path):
			full_file_name = os.path.join(path, file_name)

			if os.path.isdir(full_file_name):
				self.walk_directory(full_file_name, file_type, processor)

			if os.path.isfile(full_file_name):
				if full_file_name.endswith(ext):
					processor(full_file_name)

	def walk_directories(self, file_type, processor):
		self.walk_directory(self.root_path, file_type, processor)


class NodeDecorator(BaseDecorator):
	def output_details(self, file_name, details):
		full_file_name = "/Users/stevethehat/Development/flow/modules/%s" % file_name

		node_classes = ast_loader(full_file_name, [])
		node_classes.append(details)

		if os.path.exists(full_file_name):
			os.remove(full_file_name)

		node_classes_file = open(full_file_name, "w")
		node_classes_file.write(str(node_classes))
		node_classes_file.close()


class NodeClass(NodeDecorator):
	def __init__(self, nodetype):
		print "register nodeclass '%s'" % nodetype
		self.output_details("nodeclasses", nodetype)

class NodeAction(NodeDecorator):
	def __init__(self, description):
		print "register nodeaction '%s'" % description
		self.output_details("nodeactions", description)


if __name__ == "__main__":
	os.system("clear")
	nt = NodeTypes()
	nt.rebuild()
	nt.output()

	print "\n\n"
	print nt.definitions
		