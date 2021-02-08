from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required


# Create your models here.
from ..forms import *
# Create your views here.
from courses.models import *



class CategoryView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'adminsection/pages/categories.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    

class CreateCategoryView(CreateView):
    model = Category
    form_class = CategoryForm
    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

