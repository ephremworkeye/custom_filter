from django import template
from django.template.defaultfilters import stringfilter # for stirng filter 

# creates an instance of the django library that can be use to register ou custom filter with django
register = template.Library()

@register.filter
def explode(value, separator):
    return value.split(separator)

@register.filter
def capitalize(value):
    return value.upper()

@register.filter
@stringfilter
def string_filter_example(value):
    " This will convert an object to its string value before being passed to your function"
    return value.upper()
