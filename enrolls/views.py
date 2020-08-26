from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.views.generic import View, ListView, RedirectView


from .models import EnrollCouese
from courses.models import Course


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



class EnrollView(View):
    template_name = 'mainsite/courses/courses.html'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        return redirect('courses:courses')

    def post(self, request, *args, **kwargs):
        product_id = request.POST.get('product_id')
        
        if product_id is not None:
            product_obj = get_object_or_404(Course, id=product_id)
        if product_obj.price ==  None and product_obj.offer_price == None: 
            old_user, new_user = EnrollCouese.objects.get_or_create(user = self.request.user)

            if old_user:
                old_user.products.add(product_obj)
                messages.success(self.request, 'You are successfuly Enrolled the Course')    

            elif new_user:
                new_user.products.add(product_obj)
                messages.success(self.request, 'You are successfuly Enrolled the Course')    

            
            return redirect('dashboard:my-courses')

        messages.error(self.request, 'Something was wrong')    


        