from django.contrib import messages, auth
from django.shortcuts import render , redirect , HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView, DetailView, RedirectView, View , ListView, TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Cart
from courses.models import Course

from .forms import BillingForm

from .sslcommerz import sslcommerz_payment_gateway

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
            return redirect("cart:home")
        cart_obj, new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
            messages.success(request, 'Item Was Removed From Cart')
        else:
            cart_obj.products.add(product_obj)
            messages.success(request, 'Item Was Added On Cart')

    request.session['cart_items'] = cart_obj.products.count()
    
    return redirect("cart:cart")


class CheckoutView(View):
    """
        Provides the ability to login as a user with an email and password
    """
    form_class = BillingForm
    template_name = 'carts/checkout.html'

 
    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)


    def get_cart_item(self):
        return get_object_or_404(Cart,id = self.kwargs['id'] )

    def get(self, request, *args, **kwargs):
        form = self.form_class()
    
        context={

            'form': form,
            'cart':self.get_cart_item()
        }
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            cart_total = self.get_cart_item().total
            try:
                is_save_billing =  request.POST['is_save_billing']
            except:
                is_save_billing = False
            
            if is_save_billing:
                user = Cart.objects.filter(user = request.user).values('user')
                if user:
                
                    billing = form.save(commit=False)
                    billing.user = request.user
                    billing.save()
                    return redirect(sslcommerz_payment_gateway(form, cart_total))
            else:
                return redirect(sslcommerz_payment_gateway( form, cart_total))
                
        context={

            'form': form,
        
        }
        return render(request, self.template_name, context)

    


