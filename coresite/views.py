from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.db.models import Count,Q

from courses.models import Course

from django.conf import settings

User = settings.AUTH_USER_MODEL




from courses.models import Course
from customadmin.models import About, Testimonial


class HomeView(ListView):
    
    model = Course
    context_object_name = 'courses'
    template_name = 'mainsite/site/index.html'

    def get_queryset(self):
        return super().get_queryset().filter(is_published='True').order_by('-id')[:6]


class AboutView(ListView):
    model = About
    context_object_name = 'about'
    template_name = 'mainsite/site/about.html'

    def get_queryset(self):
        return super().get_queryset().last()


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["testimonials"] = Testimonial.objects.all()
        return context
    
    

def handler404(request, exception):
    context = {}
    response = render(request, "site/errors/404.html", context=context)
    response.status_code = 404
    return response

def handler500(request):
    context = {}
    response = render(request, "site/errors/500.html", context=context)
    response.status_code = 500
    return response

    

def search(request):

    search_post_list=Course.objects.filter(is_published='True').order_by('-id')
    query= request.GET.get('text')
    if query:
        search_post_list= search_post_list.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
        print(search_post_list)
    context={

        'courses':search_post_list,
        
    }
    return render(request,'mainsite/courses/result.html',context)