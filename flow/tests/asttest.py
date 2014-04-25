import ast, pprint, os

code = """
from flow.app.nodetypes import *

@NodeClass("page")
class Page:
	def __init__(self):
		pass

	@NodeAction("Edit")
	def edit(self):
		pass

	@NodeAction("Edit Content")
	def edit_content(self):
		pass
"""

#os.system("clear")


class v(ast.NodeVisitor):
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

tree = ast.parse(code)
os.system("clear")
test = v()
test.visit(tree)

print "classes"
print test.node_classes

print ""
print "acrions"
print test.node_actions
