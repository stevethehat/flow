from env import Env
from hierarchy import Hierarchy
from nodetypes import Nodetypes

class Flow(object):
	def __init__(self, config):
		self.env = Env(config)
		self.env.log("init Flow")
		self.hierarchy = Hierarchy(self)
		self.nodetypes = Nodetypes(self)