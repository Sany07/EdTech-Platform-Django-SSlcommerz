from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from courses.models import Category

class HomeView(ListView):
    
    model = Category
    context_object_name = 'categories'
    template_name = 'site/index.html'


class AboutView(TemplateView):
    

    template_name = 'site/about.html'