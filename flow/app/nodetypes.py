import os, ast, imp, sys, pprint, inspect
from decorators import BaseDecorator
"""
nodetypes
"""

sys.path.append("/Users/stevethehat/Development/flow")


class NodeTypes:
	def __init__(self, root_path):
		print "init NodeTypes..."
		self.root_path = root_path
		self.node_definitions_filename = os.path.join(self.root_path, "nodedefinitions")
		self.node_classes_filename = os.path.join(self.root_path, "nodeclasses")
		self.node_actions_filename = os.path.join(self.root_path, "nodeactions")
		self.definitions = {}
		self.classes = []
		self.actions = []

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

			def ensure_definition_element(key, default):
				if not(definition.has_key(key)):
					definition[key] = default

			ensure_definition_element("description", "No description specified")
			ensure_definition_element("icon", "default")
			ensure_definition_element("editor", [])
			ensure_definition_element("parentnodes", [])
			ensure_definition_element("childnodes", [])
			ensure_definition_element("actions", [])

			self.definitions[definition["name"]] = definition
		except Exception, e: 
			print "Exception processing %s\n%s" % (file_name, e.message)

	def nodemodule_processor(self, file_name):
		print "nodeclass_processor %s" % file_name

		module_file = open(file_name, "r")
		code = module_file.read()
		module_file.close()

		module_processor = ModuleProcessor()
		module_processor.visit(ast.parse(code))

		self.classes = self.classes + module_processor.node_classes
		self.actions = self.actions + module_processor.node_actions

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

		

		print "\nbuild nodedefs"
		self.walk_directories(".nodedef", self.nodedefinition_processor)

		print "\nbuild classes"
		self.walk_directories(".py", self.nodemodule_processor)

		self.process_definitions()

		save_ast(self.node_definitions_filename, self.definitions)
		save_ast(self.node_classes_filename, self.classes)
		save_ast(self.node_actions_filename, self.actions)
		self.load()

	def walk_directory(self, path, file_type, processor):
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
		print ""
		print "definitions\n%s" % pprint.pformat(self.definitions)
		print "nodeclasses\n%s" % pprint.pformat(self.classes)
		print "nodeactions\n%s" % pprint.pformat(self.actions)


class ModuleProcessor(ast.NodeVisitor):
	def __init__(self):
		self.current_class = ""
		self.node_classes = []
		self.node_actions = []

	def get_decorator_info(self, function_def, required_decorator):
		result = None
		for decorator in function_def.decorator_list:
			if str(decorator.func.id) == str(required_decorator):
				result = []
				for arg in decorator.args:
					result.append(arg.s)
		return(result)

	def process_possible_node_action(self, function_def):
		decorator_info = self.get_decorator_info(function_def, "NodeAction")

		if decorator_info != None:
			self.node_actions.append(
				{
					"arguments": decorator_info,
					"name": function_def.name,
					"class": self.current_class
				}
			)

	def process_possible_node_class(self, class_def):
		decorator_info = self.get_decorator_info(class_def, "NodeClass")

		if decorator_info != None:
			self.node_classes.append(
				{
					"class": class_def.name,
					"arguments": decorator_info
				}
			)
			self.current_class = class_def.name

	def generic_visit(self, node):
		node_type = type(node).__name__

		if node_type == "ClassDef":
			self.process_possible_node_class(node)

		if node_type == "FunctionDef":
			self.process_possible_node_action(node)

		ast.NodeVisitor.generic_visit(self, node)


class NodeDecorator(BaseDecorator):
	def __init__(self):
		pass

class NodeClass(NodeDecorator):
	def __init__(self, nodetype):
		pass

class NodeAction(NodeDecorator):
	def __init__(self, description):
		pass

if __name__ == "__main__":
	os.system("clear")
	nt = NodeTypes("/Users/stevethehat/Development/flow/modules")
	nt.rebuild()
	nt.output()	