import os
os.system("cls")

class Node:
	def __init__(self, c):
		self.c = c
		print "we have a node implementor!!!"

	def __call__(self):
		print "\n>>init object"
		c = self.c()
		print "<<init object\n"
		return(c)

class NodeAction:
	def __init__(self, f, description):
		self.f = f
		print "we have a node action implementor!!! '%s'" % description

	def __call__(self):
		print "\n>>method call"
		f = self.f(self)
		print "<<method call\n"
		return(f)

@Node
class Page:
	def __init__(self):
		print "in page init"

	@NodeAction("Edit Content")
	def EditContent(self):
		print "Edit content on page"




page = Page()
page.EditContent()


print "decorators test"