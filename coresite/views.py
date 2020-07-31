from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from courses.models import Course

class HomeView(ListView):
    
    model = Course
    context_object_name = 'courses'
    template_name = 'site/index.html'

    def get_queryset(self):
        return self.model.objects.order_by('-id')[:6]


class AboutView(TemplateView):
    

    template_name = 'site/about.html'