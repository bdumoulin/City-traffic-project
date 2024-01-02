from django import template

register = template.Library()


@register.filter(name='get_travel_time')
def get_travel_time(path):
    return path.calculate_real_travel_time('rain', '0-7')
