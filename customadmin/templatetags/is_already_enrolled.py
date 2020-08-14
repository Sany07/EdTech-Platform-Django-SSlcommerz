from django import template

from enrolls.models import EnrollCouese

register = template.Library()


@register.simple_tag(name='is_already_enrolled')
def is_already_enrolled(user, course):
    if user.is_authenticated:

        enrolled = EnrollCouese.objects.filter(user=user, products = course)
        if enrolled:
            return True
        else:
            return False
    return False 