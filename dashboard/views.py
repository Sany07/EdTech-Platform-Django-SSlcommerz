from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView, View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import Http404

from enrolls.models import EnrollCouese
from courses.models import Course
from courses.decorators import user_is_instructor, user_is_student




class DashboardView(View):
    
    template_name = 'site/dashboard.html'


    def get(self, request, *args, **kwargs):
        total_course = None
        if request.user.role == 'tea':
            total_course = Course.objects.filter(instructor = self.request.user).count()
            
        elif request.user.role == 'stu':
            
            total_course = EnrollCouese.objects.filter(user = self.request.user).values('products').count()
        context = {
            'total_course':total_course
        }
        return render(request, self.template_name, context)   

    def post(self, request, *args, **kwargs):
        return render(request, self.template_name)    


class InstructorCourseListView(ListView):
    model = Course
    context_object_name = 'mycourses'
    template_name = "site/instructor-courses.html"

    @method_decorator(login_required)
    @method_decorator(user_is_instructor)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get_queryset(self):
        return self.model.objects.filter(instructor = self.request.user)

class MyEnrolledCourseListView(ListView):
    model = EnrollCouese
    context_object_name = 'mycourses'
    template_name = "site/my-courses.html"

    @method_decorator(login_required)
    @method_decorator(user_is_student)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def get_queryset(self):
        return self.model.objects.filter(user = self.request.user).first()

    


class StartCourseView(DetailView):

    model= Course
    context_object_name = 'course'
    template_name = 'site/classroom.html'

    @method_decorator(login_required)
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def get_object(self, queryset=None):
        obj = super(StartCourseView, self).get_object(queryset=queryset)
        
        if obj is not None:
            enrolledOrnot = get_object_or_404(EnrollCouese, user = self.request.user, products = obj)
            return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("Course doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)







