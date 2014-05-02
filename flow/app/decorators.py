class BaseDecorator:
	def __call__(self, f):
		#if self.oncall:
		#	self.oncall(f)
		def wrapper(*args):
			wrapped_f = f(*args)
			return(wrapped_f)
		return(wrapper)

def cacheprop(fn):
    attr_name = '_lazy_' + fn.__name__
    @property
    def _cacheprop(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, fn(self))
        return getattr(self, attr_name)
    return _cacheprop