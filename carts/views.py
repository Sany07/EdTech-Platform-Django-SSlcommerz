from django.contrib import messages, auth
from django.shortcuts import render, redirect, HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView, DetailView, RedirectView, View, ListView, TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import JsonResponse

from courses.models import Course
from .models import Cart
from .forms import BillingForm
from .sslcommerz import sslcommerz_payment_gateway


class CartView(ListView):
    model = Cart
    template_name = "mainsite/carts/cart.html"

    def get_queryset(self):
        return self.model.objects.new_or_get(self.request)



def cart_detail_api(request):
    """cart api for refresh cart items on CartView via ajax call"""
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = [{
            "id": x.id,
            "url": x.get_absolute_url(),
            "name": x.title, 
            "price": x.price
            } 
            for x in cart_obj.products.all()]
    cart_data  = {"products": products, "subtotal": cart_obj.subtotal, "total": cart_obj.total}
    return JsonResponse(cart_data)


def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0

    for product in products:
        if product.price is not None or product.offer_price is not None:
            total += product.price
            cart_obj.total = total
    cart_obj.save()

    context = {
        'cart': cart_obj

    }
    return render(request, "mainsite/carts/cart.html", context)


def cart_update(request):

    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Course.objects.get(id=product_id)

        except Product.DoesNotExist:
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            added = False
            # messages.success(request, 'Item Was Removed From Cart')
        else:
            cart_obj.products.add(product_obj)
            added = True
            # messages.success(request, 'Item Was Added On Cart')

        request.session['cart_items'] = cart_obj.products.count()

        if request.is_ajax(): # Asynchronous JavaScript And XML / JSON
            json_data = {
                "added": added,
                "removed": not added,
                "CartItemCount": cart_obj.products.count()
            }
            return JsonResponse(json_data)
    return redirect("cart:cart")






class CheckoutView(View):
    """
        Provides the ability to checkout if user is authenticated
    """
    form_class = BillingForm
    template_name = 'mainsite/carts/checkout.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get_cart_item(self):
        return get_object_or_404(Cart, id=self.kwargs['id'])


    def get(self, request, *args, **kwargs):
        form = self.form_class()

        context = {

            'form': form,
            'cart': self.get_cart_item()
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            cart = self.get_cart_item()
            # cart_total = self.get_cart_item().total
            try:
                is_save_billing = request.POST['is_save_billing']
            except:
                is_save_billing = False

            user = Cart.objects.filter(user=request.user).values('user')
            if user:
                if is_save_billing:

                        billing = form.save(commit=False)
                        billing.user = request.user
                        billing.save()
                        return redirect(sslcommerz_payment_gateway(form, cart, request.user))
                else:
                    return redirect(sslcommerz_payment_gateway(form, cart, request.user))

        context = {

            'form': form,
            'cart': self.get_cart_item()
        }
        return render(request, self.template_name, context)




    