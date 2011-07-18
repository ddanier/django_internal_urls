from django import template
from django.conf import settings

register = template.Library()


class InternalUrlNode(template.Node):
	def __init__(self, module, args, kwargs):
		self.module = module
		self.args, self.kwargs = args, kwargs
	
	def render(self, context):
		return self.module(self.args, self.kwargs)


@register.tag
def iurl(parser, token):
	"""Display a form and handles form-saving
	
	{% iurl module arg1 arg2 kwarg1=foo kwarg2=bar %}
	"""
	from django_internal_urls.utils import parse_args
	from django_internal_urls import modules
	parts = token.split_contents()
	if len(parts) < 2:
		raise template.TemplateSyntaxError("%r tag requires as least one argument" % parts[0])
	module_name = parts[1]
	try:
		module = modules.get(module_name)
	except modules.ModuleDoesNotExist:
		raise template.TemplateSyntaxError("%r tag requires valid module as first argument" % parts[0])
	args, kwargs = parse_args(parts[2:])
	return InternalUrlNode(module, args, kwargs)

