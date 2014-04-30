from nodestore_file import NodeStore_File

class Node:
	def __init__(self, hierarchy, uid):
		self.hierarchy = hierarchy
		self.uid = uid
		self.data = self.hierarchy.store.get(uid)

	def __repr__(self):
		return(
			str(
				{"uid": self.uid, "data": self.data}
			)
		)
