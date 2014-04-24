"""
nodetypes
"""

class NodeTypes:
	def __init__():
		pass

	def rebuild():
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
		