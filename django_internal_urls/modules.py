class ModuleDoesNotExist(KeyError):
	pass

_modules = {}

def register(name, module):
	_modules[name] = module

def get(name):
	try:
		return _modules[name]
	except KeyError:
		raise ModuleDoesNotExist()

def get_all():
	return _modules

def django_url(args, kwargs):
	from django.core.urlresolvers import reverse, NoReverseMatch
	if len(args) < 1:
		return ''
	url = args[0]
	args = args[1:]
	try:
		return reverse(url, args=args, kwargs=kwargs)
	except NoReverseMatch:
		return ''

register('url', django_url)

