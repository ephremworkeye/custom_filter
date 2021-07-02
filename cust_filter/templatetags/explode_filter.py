from django import template

# creates an instance of the django library that can be use to register ou custom filter with django
register = template.Library()

@register.filter
def explode(value, separator):
    return value.split(separator)