from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import View, DeleteView
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib import messages

from .models import Transaction
from accounts.models import CustomUser
from carts.models import Cart
from enrolls.models import EnrollCouese



@method_decorator(csrf_exempt, name='dispatch')
class CheckoutSuccessView(View):
    model = Transaction
    template_name = 'mainsite/carts/checkout-success.html'

    
    def get(self, request, *args, **kwargs):

        user = get_object_or_404(CustomUser, id=request.user.id)
        transaction = Transaction.objects.filter(user = request.user.id).last()
        print('transaction')
        print(transaction)
        print(request.user)
        del self.request.session['cart_items'] #here deleting the total items on cart session 

        return render(request, self.template_name,{'transaction':transaction})

    def post(self, request, *args, **kwargs):

        data = self.request.POST
        user = get_object_or_404(CustomUser, id=data['value_a']) #value_a is a user instance
        cart = get_object_or_404(Cart, id = data['value_b'] ) #value_b is a user cart instance
        try:
            Transaction.objects.create(
                user = user ,
                tran_id=data['tran_id'],
                val_id=data['val_id'],
                amount=data['amount'],
                card_type=data['card_type'],
                card_no=data['card_no'],
                store_amount=data['store_amount'],
                bank_tran_id=data['bank_tran_id'],
                status=data['status'],
                tran_date=data['tran_date'],
                currency=data['currency'],
                card_issuer=data['card_issuer'],
                card_brand=data['card_brand'],
                card_issuer_country=data['card_issuer_country'],
                card_issuer_country_code=data['card_issuer_country_code'],
                verify_sign=data['verify_sign'],
                verify_sign_sha2=data['verify_sign_sha2'],
                currency_rate=data['currency_rate'],
                risk_title=data['risk_title'],
                risk_level=data['risk_level'],

            )
        except:
            messages.success(request,'Payment Successfull')

        #Redirect on this view because we have to delete the cart items total count
            return redirect('billing:success')

        old_user, new_user = EnrollCouese.objects.get_or_create(user = user)
 
        if old_user:
            for item in cart.products.all():
                old_user.products.add(item)
                
        elif new_user:
            for item in cart.products.all():
                new_user.products.add(item)
        
        #delete the individual cart
        cart = cart.delete()
        messages.success(request,'Payment Successfull')

        #Redirect on this view because we have to delete the cart items total count
        return redirect('billing:success')

@method_decorator(csrf_exempt, name='dispatch')
class CheckoutFaildView(View):
    template_name = 'mainsite/carts/checkout-faild.html'


    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        return redirect('billing:faild')


class InvoiceView(DeleteView):
    model = Transaction
    slug_field = 'tran_id'
    slug_url_kwarg = 'tran_id'
    context_object_name = 'transaction'
    template_name = 'mainsite/carts/invoice.html'