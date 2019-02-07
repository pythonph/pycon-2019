import random

from django import template

register = template.Library()


@register.simple_tag
def blend_class(seed=None, *exclude):
    if seed:
        random.seed(int(seed))
    exclude = set(exclude)
    all_colors = {
        'red',
        'orange',
        'blue',
        'yellow',
        'purple',
        'green',
        'pink',
        'blue-yellow',
        'pink-yellow',
        # 'red-blue',
    }
    colors = list(all_colors - exclude)
    color = random.choice(colors)
    return 'blend-{}'.format(color)
