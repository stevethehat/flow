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
	def generic_visit(self, node):
		if type(node).__name__ == "FunctionDef":
			for decorator in node.decorator_list:
				#print "decorator = %s" % dir(decorator)
				#print dir(decorator.func)
				print decorator.func.id
				for arg in decorator.args:
					print "%s" % dir(arg)
					print arg.s

		#print type(node).__name__
		#print node
		#print dir(node)
		ast.NodeVisitor.generic_visit(self, node)

tree = ast.parse(code)
#print ast.walk(tree)
#print dir(tree)

test = v()
test.visit(tree)
#print pprint.pformat(tree)