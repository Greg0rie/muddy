from django import template
from rango.models import Category

register = template.Library()

@register.inclusion_tag('rango/cars.html')
def get_category_list(car=None):
    return{'cars': Category.objects.all(),
           'act_car': car}