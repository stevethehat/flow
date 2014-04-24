import os, ast, imp, sys, pprint
from decorators import BaseDecorator
"""
nodetypes
"""

sys.path.append("/Users/stevethehat/Development/flow")

def load_ast(full_file_name, default):
	result = default
	if os.path.exists(full_file_name):
		object_file = open(full_file_name, "r")
		result = ast.literal_eval(object_file.read())
		object_file.close()
	return(result)

def save_ast(full_file_name, obj):
	if os.path.exists(full_file_name):
		os.remove(full_file_name)

	object_file = open(full_file_name, "w")
	object_file.write(str(obj))
	object_file.close()

class NodeTypes:
	def __init__(self, root_path):
		print "init NodeTypes..."
		self.root_path = root_path
		self.node_definitions_filename = os.path.join(self.root_path, "nodedefinitions")
		self.node_classes_filename = os.path.join(self.root_path, "nodeclasses")
		self.node_actions_filename = os.path.join(self.root_path, "nodeactions")
		self.definitions = {}

		if not(os.path.exists(self.node_definitions_filename)) or not(os.path.exists(self.node_classes_filename)) or not(os.path.exists(self.node_actions_filename)):
			self.rebuild()

		self.load()

	def load(self):
		self.definitions = load_ast(self.node_definitions_filename, {})
		self.classes = load_ast(self.node_classes_filename, [])
		self.actions = load_ast(self.node_actions_filename, [])

	def nodedefinition_processor(self, file_name):
		print "nodedefinition_processor %s" % file_name
		try:
			definition_file = open(file_name, "r")
			definition = ast.literal_eval(definition_file.read())
			definition_file.close()

			if not(definition.has_key("parentnodes")):
				definition["parentnodes"] = []

			if not(definition.has_key("childnodes")):
				definition["childnodes"] = []

			if not(definition.has_key("actions")):
				definition["actions"] = []


			self.definitions[definition["name"]] = definition
		except Exception, e: 
			print "Exception processing %s\n%s" % (file_name, e.message)

	def nodeclass_processor(self, file_name):
		print "nodeclass_processor %s" % file_name
		imp.load_source("page", file_name)

	def process_definitions(self):
		def process_parent_nodes(definition):
			parent_nodes = definition["parentnodes"]
			for parent_node in parent_nodes:
				self.definitions[parent_node]["childnodes"].append(definition["name"])



		for name in self.definitions:
			definition = self.definitions[name]
			process_parent_nodes(definition)

		pass

	def rebuild(self):
		print "rebuild nodetypes..."

		if os.path.exists(self.node_definitions_filename):
			os.remove(self.node_definitions_filename)

		if os.path.exists(self.node_classes_filename):
			os.remove(self.node_classes_filename)

		if os.path.exists(self.node_actions_filename):
			os.remove(self.node_actions_filename)

		print "\n\nbuild nodedefs"
		self.walk_directories(".nodedef", self.nodedefinition_processor)

		print "\n\nbuild classes"
		self.walk_directories(".py", self.nodeclass_processor)

		self.process_definitions()

		save_ast(self.node_definitions_filename, self.definitions)
		self.load()

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

	def output(self):
		print "definitions\n%s" % pprint.pformat(self.definitions)
		print "nodeclasses\n%s" % pprint.pformat(self.classes)
		print "nodeactions\n%s" % pprint.pformat(self.actions)

class NodeDecorator(BaseDecorator):
	def output_details(self, file_name, details):
		full_file_name = "/Users/stevethehat/Development/flow/modules/%s" % file_name

		node_objs = load_ast(full_file_name, [])
		node_objs.append(details)
		save_ast(full_file_name, node_objs)

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
	nt = NodeTypes("/Users/stevethehat/Development/flow/modules")
	nt.rebuild()
	nt.output()	