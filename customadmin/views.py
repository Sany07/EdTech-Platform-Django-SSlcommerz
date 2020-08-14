from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.conf import settings 

from django.contrib.admin.views.decorators import staff_member_required


# Create your models here.

User = settings.AUTH_USER_MODEL
# Create your views here.
from courses.models import Course, Lesson
from accounts.models import CustomUser


class DashBoardView(TemplateView):
    
    template_name = 'adminsection/pages/dashboard.html'


    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    
    def get_total_statistics(self):      
        users = CustomUser.objects.all()
        totalusers = users.count()
        totalteachers = users.filter(role = "tea").count()
        totalstudents = users.filter(role = "stu").count()
        totalcourses = Course.objects.all().count()
        return totalusers, totalteachers, totalstudents, totalcourses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = self.get_total_statistics()
        context["totalusers"] = results[0]
        context["totalteachers"] = results[1]
        context["totalstudents"] = results[2]
        context["totalcourses"] = results[3]

        return context


class TotalUsersView(ListView):
    model = CustomUser
    context_object_name = 'users'
    template_name = 'adminsection/pages/users.html'


    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class TotalInstructorsView(ListView):
    model = CustomUser
    context_object_name = 'instructors'
    template_name = 'adminsection/pages/instructors.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_queryset(self):
        return super().get_queryset().filter(role='tea')

class TotalStudentsView(ListView):
    model = CustomUser
    context_object_name = 'students'
    template_name = 'adminsection/pages/students.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_queryset(self):
        return super().get_queryset().filter(role='stu')

class CoursesView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'adminsection/pages/courses.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    

class NewCoursesView(ListView):
    model = Course
    context_object_name = 'courses'
    template_name = 'adminsection/pages/newcourses.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["new_courses"] = super().get_queryset().filter(is_published='False')
        return context


class CourseDetailView(DetailView):
    model = Course
    context_object_name = 'course'
    template_name = 'adminsection/pages/course-detail.html'

    def get_total_lecture(self):               
        return Lesson.objects.filter(course=self.object).values('video_link').count()
        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_lecture'] = self.get_total_lecture()

        return context