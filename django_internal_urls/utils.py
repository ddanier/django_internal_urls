def parse_args(options):
	args = []
	kwargs = {}
	if not options:
		return args, kwargs
	for option in options:
		if '=' in option:
			key, value = option.split('=', 1)
			kwargs[key] = value
		else:
			args.append(option)
	return args, kwargs

def resolve(module, args, kwargs):
	from django_internal_urls import modules
	try:
		handler = modules.get(module)
	except module.ModuleDoesNotExist:
		return ''
	return handler(args, kwargs)
