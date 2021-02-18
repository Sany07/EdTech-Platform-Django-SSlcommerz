from django import template

from courses.models import Course

register = template.Library()


@register.simple_tag(name='is_category_has_course')
def is_category_has_course(category):
    has_course = Course.objects.filter(category=category, is_published='True')
    if has_course:
        return True
    else:
        return False