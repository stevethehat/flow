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

	def other_method(self):
		pass

class NotANodeClass():
	def __init__(self):
		pass