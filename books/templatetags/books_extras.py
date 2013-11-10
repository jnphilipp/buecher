from django.template import Library

register = Library()

@register.filter
def is_false(arg):
	return arg is False

@register.filter
def list_title(obj, epk):
	return obj.get_list_title(epk)