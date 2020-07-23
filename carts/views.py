from django.contrib import messages, auth
from django.shortcuts import render , redirect , HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView, DetailView, RedirectView, View , ListView, TemplateView, FormView


from .models import Cart
from courses.models import Course


class CartView(ListView):
    model = Cart
    template_name = "carts/cart.html"
    
    def get_queryset(self):
        return self.model.objects.new_or_get(self.request)
    

def cart_home(request):
    cart_obj, new_obj = Cart.objects.new_or_get(request)
    products = cart_obj.products.all()
    total = 0
    for x in products:
        total += x.price
        cart_obj.total = total
    cart_obj.save()
    
    context = {
        'cart':cart_obj

    }
    return render(request, "carts/cart.html", context)


def cart_update(request):
    
    
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = Course.objects.get(id=product_id)
        except Product.DoesNotExist:
            print("Show message to user, product is gone?")
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)  

    request.session['cart_items'] = cart_obj.products.count()
    
    return redirect("cart:cart")


def checkout(request, id):

    chart = Cart.objects.filter(id = id)
 
    return render(request, "carts/checkout.html")

# class CheckoutView(DetailView):
#     model = Cart
#     template_name = 'carts/checkout.html'


