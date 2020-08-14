from django import template

from carts.models import Cart

register = template.Library()


@register.simple_tag(name='add_or_remove_from_cart')
def add_or_remove_from_cart(request,course):
    cart_obj, new_obj  = Cart.objects.new_or_get(request)

    if course in cart_obj.products.all():
        return True
    else:
        return False

