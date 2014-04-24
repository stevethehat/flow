import os
os.system("cls")

class BaseDecorator:
	def __init__(self):
		self._message = ""

	def __call__(self, f):
		def wrapper(*args):
			print "\n>>%s" % self._message
			wrapped_f = f(*args)
			print "<<%s\n" % self._message
			return(wrapped_f)
		return(wrapper)


class NodeClass(BaseDecorator):
	def __init__(self, nodetype):
		print "we have a node implementor!!! '%s'" % nodetype
		self._message = "NodeClass init"

class NodeAction(BaseDecorator):
	def __init__(self, description):
		print "we have a node action implementor!!! '%s'" % description
		self._message = "NodeAction call"


@NodeClass("page")
class Page:
	def __init__(self):
		print "in page init"

	@NodeAction("Edit Content")
	def EditContent(self):
		print "Edit content on page"

print "test page 1"
page = Page()
page.EditContent()

print "test page 2"
page2 = Page()
page2.EditContent()

print "decorators test"