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


