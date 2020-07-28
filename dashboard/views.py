from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
from django.http import Http404

from enrolls.models import EnrollCouese
from courses.models import Course

class MyCourseListView(ListView):
    model = EnrollCouese
    context_object_name = 'mycourses'
    template_name = "site/my-courses.html"

    @method_decorator(login_required)
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







