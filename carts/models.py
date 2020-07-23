from decimal import Decimal
from django.shortcuts import get_object_or_404
from django.conf import settings
from django.db import models
from django.db.models.signals import pre_save, post_save, m2m_changed


from courses.models import Course


User = settings.AUTH_USER_MODEL


class CartManager(models.Manager):
    def new_or_get(self, request):
        cart_id = request.session.get("cart_id", None)
        qs = self.get_queryset().filter(id=cart_id)
        if qs.count() == 1:
            new_obj = False
            cart_obj = qs.first()
            if cart_obj.user is None and request.user.is_authenticated:
                cart_obj.user = request.user
                cart_obj.save()
        else:
            try:
                cart_obj = Cart.objects.create(user=request.user)
            except:
                cart_obj = Cart.objects.create(user=None)

            new_obj = True
            request.session['cart_id'] = cart_obj.id
        return cart_obj, new_obj



class Cart(models.Model):
    user        = models.ForeignKey(User, null=True, blank=True, on_delete=models.DO_NOTHING)
    products    = models.ManyToManyField(Course, blank=True)
    subtotal    = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    total       = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    updated     = models.DateTimeField(auto_now=True)
    timestamp   = models.DateTimeField(auto_now_add=True)

    objects = CartManager()

    def __str__(self):
        return str(self.id)

def m2m_changed_cart_receiver(sender, instance, action, *args, **kwargs):
    if action == 'post_add' or action == 'post_remove' or action == 'post_clear':
        products = instance.products.all()
        total = 0
        for x in products:
            if x.offer_price:
                total += x.offer_price
            else:
                total += x.price
                
        if instance.subtotal != total:
            instance.subtotal = total
            instance.save()
m2m_changed.connect(m2m_changed_cart_receiver, sender=Cart.products.through)


def pre_save_cart_receiver(sender, instance, *args, **kwargs):
    if instance.subtotal > 0:
        instance.total = Decimal(instance.subtotal) * Decimal(1) # 8% tax
    else:
        instance.total = 0.00
pre_save.connect(pre_save_cart_receiver, sender=Cart)

 

