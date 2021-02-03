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


class NewCoursesView(ListView):
    model = Category
    context_object_name = 'Category'
    template_name = 'adminsection/pages/new-courses.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(is_published=False)
    


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


def approvedOrReject(request):

    course_id = request.POST.get('course_id')
    if course_id is not None:
        try:
            course_obj = Course.objects.get(id=course_id)
            course_obj.is_published = True
            course_obj.save()
            return redirect("customadmin:courses")
        except Course.DoesNotExist:
            raise Http404()

        # if request.is_ajax(): # Asynchronous JavaScript And XML / JSON
        #     json_data = {
        #         "added": added,
        #         "removed": not added,
        #         "CartItemCount": cart_obj.products.count()
        #     }
        #     return JsonResponse(json_data)
    return redirect("customadmin:dashboard")