
# from django.contrib.auth.base_user import BaseUserManager
# from django.db import models

# from carts.models import Cart

# class CartManager(models.Manager):
#     def new_or_get(self, request):
#         cart_id = request.session.get("cart_id", None)
#         qs = self.get_queryset().filter(id=cart_id)
#         if qs.count() == 1:
#             new_obj = False
#             cart_obj = qs.first()
#             if request.user.is_authenticated() and cart_obj.user is None:
#                 cart_obj.user = request.user
#                 cart_obj.save()
#         else:
#             cart_obj = Cart.objects.new(user=request.user)
#             new_obj = True
#             request.session['cart_id'] = cart_obj.id
#         return cart_obj, new_obj

#     def new(self, user=None):
#         user_obj = None
#         if user is not None:
#             if user.is_authenticated():
#                 user_obj = user
#         return self.model.objects.create(user=user_obj)