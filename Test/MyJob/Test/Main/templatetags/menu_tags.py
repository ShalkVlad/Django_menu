from django import template
from ..models import MenuItem

register = template.Library()


@register.simple_tag
def draw(menu_name):
    items = MenuItem.objects.filter(title=menu_name).select_related('parent').prefetch_related('children')
    return {
        'menu_items': items
    }
