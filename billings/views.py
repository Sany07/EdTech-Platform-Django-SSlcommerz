from django.shortcuts import render

# Create your views here.
class CheckoutView(View):
    """
        Provides the ability to login as a user with an email and password
    """
    # form_class = Cart
    template_name = 'carts/checkout.html'

    success_url = '/'
    # form_class = UserLoginForm
    

    extra_context = {
        'title': 'Login'
    }

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        # if self.request.user.is_authenticated:
        #     return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    # def get_success_url(self):
    #     if 'next' in self.request.GET and self.request.GET['next'] != '':
    #         return self.request.GET['next']
    #     else:
    #         return self.success_url

    # def get(self, request, *args, **kwargs):
    #     form = self.form_class(initial=self.initial)
    #     return render(request, self.template_name, {'form': form})

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #     if form.is_valid():
    #         # <process form cleaned data>
    #         return HttpResponseRedirect('/success/')

    #     return render(request, self.template_name, {'form': form})



def checkout_view(request):
    if request.method == "GET":
        amount = request.GET.get('amount')
        if amount != None:
            print(amount)

            settings = {'store_id': 'graph5f0ae5eb36392',
                        'store_pass': 'graph5f0ae5eb36392@ssl', 'issandbox': True}
            sslcommez = SSLCOMMERZ(settings)
            post_body = {}
            post_body['total_amount'] = amount
            post_body['currency'] = "BDT"
            post_body['tran_id'] = id_generator()
            post_body['success_url'] = 'http://127.0.0.1:8000/success/'
            post_body['fail_url'] = '/failed/'
            post_body['cancel_url'] = '/cancle/'
            post_body['emi_option'] = 0
            post_body['cus_name'] = "Nasim"
            post_body['cus_email'] = "xyz.jgc@gmail.com"
            post_body['cus_phone'] = "017961533690"
            post_body['cus_add1'] = "Dhaka"
            post_body['cus_city'] = "Dhaka"
            post_body['cus_country'] = "Bangladesh"
            post_body['shipping_method'] = "NO"
            post_body['multi_card_name'] = ""
            post_body['num_of_item'] = 1
            post_body['product_name'] = "Test"
            post_body['product_category'] = "Test Category"
            post_body['product_profile'] = "general"

            response = sslcommez.createSession(post_body)
            return redirect('https://sandbox.sslcommerz.com/gwprocess/v4/gw.php?Q=pay&SESSIONKEY=' + response["sessionkey"])
       
            
        return render(request, "checkout.html", {})