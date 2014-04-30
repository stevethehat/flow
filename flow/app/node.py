from nodestore_file import NodeStore_File

class Node:
	def __init__(self, hierarchy, uid, data = None):
		self.hierarchy = hierarchy
		self.uid = uid
		if data != None:
			self.data = data
		else:
			self.data = self.hierarchy.store.get(uid)

	def children(self):
		children = self.hierarchy.store.children(self.uid)
		print children

	def edit(self):
		return("the result of the edit...")

	def __repr__(self):
		return(
			str(
				{"uid": self.uid, "data": self.data}
			)
		)
