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


# def courseview(request, id):
#     course = None
#     # if EnrollCouese.objects.filter(user = request.user, products = id):
#     #     course = get_object_or_404(Course, id=id)
    
#     return render(request, 'courses/start-course.html', {'course':course})
    

class StartCourseView(DetailView):

    model= Course
    context_object_name = 'course'
    template_name = 'courses/start-course.html'

    # def get_queryset(self):
        
    #     course = self.model.objects.filter(slug = self.kwargs['slug'])
        
    #     a=EnrollCouese.objects.filter(user = self.request.user, products = course.first().id)
    #     if a:
    #         return course
    #     raise Http404('course not found')
    
    def get_object(self, queryset=None):
        obj = super(StartCourseView, self).get_object(queryset=queryset)
        print(obj)
        if obj is not None:
            enrolledOrnot = get_object_or_404(EnrollCouese, user = self.request.user, products = obj)
            return obj

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            print(self.object)
        except Http404:
            raise Http404("Course doesn't exists")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)







