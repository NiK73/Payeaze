from django import template

register = template.Library()

@register.simple_tag
def currentorderid(val=7):
	val = 7
	return val