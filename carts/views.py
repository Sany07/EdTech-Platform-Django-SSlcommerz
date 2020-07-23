from django.contrib import messages, auth
from django.shortcuts import render , redirect , HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView, DetailView, RedirectView, View , ListView, TemplateView, FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from .models import Cart
from courses.models import Course

from .forms import BillingForm

from sslcommerz_lib import SSLCOMMERZ
from django.conf import settings

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


# def checkout(request, id):

#     chart = Cart.objects.filter(id = id)
 
#     return render(request, "carts/checkout.html")
    

class CheckoutView(View):
    """
        Provides the ability to login as a user with an email and password
    """
    form_class = BillingForm
    template_name = 'carts/checkout.html'

    success_url = '/'


    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        form = self.form_class()
        
        
        cart= get_object_or_404(Cart,id = self.kwargs['id'] )

        context={

            'form': form,
            'cart':cart
        }
        return render(request, self.template_name,context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST or None)
        if form.is_valid():
            is_save_billing = False
            is_save_billing =  request.POST['is_save_billing']

            if is_save_billing:
                user = Cart.objects.filter(user = request.user).values('user')
                if user:
                
                    billing = form.save(commit=False)
                    billing.user = request.user
                    billing.save()
                    return redirect(ssl(form))
            else:
                print("not save")
                

        context={

            'form': form,
        
        }
        return render(request, self.template_name, context)

    

def ssl(request):
    print(request.data["email"])
    settings = {'store_id': 'graph5f0ae5eb36392',
                'store_pass': 'graph5f0ae5eb36392@ssl', 'issandbox': True}
    sslcommez = SSLCOMMERZ(settings)
    post_body = {}
    post_body['total_amount'] = '1000'
    post_body['currency'] = "BDT"
    post_body['tran_id'] = "aofhoaiao"
    post_body['success_url'] = 'http://127.0.0.1:8000/'
    post_body['fail_url'] = 'http://127.0.0.1:8000/'
    post_body['cancel_url'] = 'http://127.0.0.1:8000/'
    post_body['emi_option'] = 0
    post_body['cus_name'] = request.data["full_name"]
    post_body['cus_email'] = request.data["email"]
    post_body['cus_phone'] = request.data["phone"]
    post_body['cus_add1'] = request.data["address"]
    post_body['cus_city'] = request.data["address"]
    post_body['cus_country'] = 'Bangladesh'
    post_body['shipping_method'] = "NO"
    post_body['multi_card_name'] = ""
    post_body['num_of_item'] = 1
    post_body['product_name'] = "Test"
    post_body['product_category'] = "Test Category"
    post_body['product_profile'] = "general"

    response = sslcommez.createSession(post_body)
    return 'https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"]

