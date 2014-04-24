class BaseDecorator:
	def __call__(self, f):
		self.oncall(f)
		def wrapper(*args):
			wrapped_f = f(*args)
			return(wrapped_f)
		return(wrapper)
