import os
"""
nodetypes
"""

class NodeTypes:
	def __init__(self):
		print "init NodeTypes..."

		self.definitions = []

	def nodedefinition_processor(self, file_name):
		print "nodedefinition_processor %s" % file_name

	def nodeclass_processor(self, file_name):
		print "nodeclass_processor %s" % file_name

	def rebuild(self):
		print "rebuild nodetypes..."
		print "\n\nbuild nodedefs"
		self.walk_directories(".nodedef", self.nodedefinition_processor)
		print "\n\nbuild classes"
		self.walk_directories(".py", self.nodeclass_processor)

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
		root_path = "/Users/stevethehat/Development/flow/modules"
		self.walk_directory(root_path, file_type, processor)

		"""
		test_dir = os.path.dirname(os.path.realpath(__file__))
		print "run tests in '%s'...\n\n" % test_dir

		for file_name in os.listdir(test_dir):
			if file_name.endswith(".py") and not(file_name == "admintest.py"):
				print "looking for tests in '%s'...\n" % file_name

				test_module = __import__(file_name[:-3])

				for test_member in getmembers(test_module):
					test_name = test_member[0]
					test_function = test_member[1]

					if(test_name.startswith("test_")):
						if isfunction(test_function):
							print test_member
							function = getattr(test_module, test_name)
							function(self)
		"""

os.system("cls")
nt = NodeTypes()
nt.rebuild()
		

"""
class Singleton(object):
	__instance = None

	def __new__(cls):
		if cls.__instance == None:
			__instance = object.__new__(cls)
			__instance.name = "the one"
		return(__instance)


test1 = Singleton()
test2 = Singleton()

print test1
print test2


"""