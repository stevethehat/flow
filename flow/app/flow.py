from env import Env
from hierarchy import Hierarchy

class Flow():
	def __init__(self, config):
		self.env = Env(config)
		self.env.log("init Flow")
		self.hierarchy = Hierarchy(self.env)