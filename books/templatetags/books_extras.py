from django.template import Library
from django.utils.numberformat import format

register = Library()

@register.filter
def is_false(arg):
	return arg is False

@register.filter
def list_title(obj, epk):
	return obj.get_list_title(epk)

@register.filter
def floatdot(value, decimal_pos=2):
	if not value:
		return format(0, ",", decimal_pos)
	else:
		return format(value, ",", decimal_pos)
floatdot.is_safe = True