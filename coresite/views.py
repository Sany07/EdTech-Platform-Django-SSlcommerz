from django.shortcuts import render
from django.views.generic import ListView, TemplateView




from django.conf import settings

User = settings.AUTH_USER_MODEL




from courses.models import Course


class HomeView(ListView):
    
    model = Course
    context_object_name = 'courses'
    template_name = 'mainsite/site/index.html'

    def get_queryset(self):
        return self.model.objects.order_by('-id')[:6]


class AboutView(TemplateView):
    

    template_name = 'mainsite/site/about.html'





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