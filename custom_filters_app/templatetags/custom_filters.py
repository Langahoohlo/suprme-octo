from django import template

register = template.Library()

@register.filter(name='get_last_login')
def get_last_login(dictionary, key):
    return dictionary.get(key)
