
from django.views.generic import ListView, DetailView, FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required

from accounts.models import CustomUser, Profile
from courses.models import Course
from enrolls.models import EnrollCouese



class AllUsersView(ListView):
    model = CustomUser
    context_object_name = 'users'
    template_name = 'adminsection/pages/all-users.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

class AllInstructorsView(ListView):
    model = CustomUser
    context_object_name = 'instructors'
    template_name = 'adminsection/pages/all-instructors.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(role='tea')


class AllStudentsView(ListView):
    model = CustomUser
    context_object_name = 'students'
    template_name = 'adminsection/pages/all-students.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:student-register')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        return super().get_queryset().filter(role='stu')


class ProfileView(DetailView):
    model = CustomUser
    context_object_name = 'profile'
    template_name = 'adminsection/pages/profile.html'

    def get_courses_list(self):
        if self.object.role == 'tea':

            courses_list = Course.objects.filter(instructor=self.object)
            total_courses = courses_list.count()
            return courses_list, total_courses
            
        elif self.object.role == 'stu':

            courses_list = EnrollCouese.objects.filter(user=self.object).first()
            total_courses = courses_list.products.all().count()
            print(total_courses)
            return courses_list, total_courses                                                             
                                                                        

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['courses'] = self.get_courses_list()[0]
        context['total_courses'] = self.get_courses_list()[1]
        return context




# class EditProfileView(UpdateView):
#     model = CustomUser
#     # form_class = EmployeeProfileUpdateForm
#     context_object_name = 'employee'
#     # template_name = 'jobs/employee/edit-profile.html'
#     success_url = reverse_lazy('/')

#     @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
#     @method_decorator(staff_member_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(self.request, *args, **kwargs)

#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_object()
#         except Http404:
#             raise Http404("User doesn't exists")
#         # context = self.get_context_data(object=self.object)
#         return self.render_to_response(self.get_context_data())

#     def get_object(self, queryset=None):
#         obj = self.request.user
#         print(obj)
#         if obj is None:
#             raise Http404("Job doesn't exists")
#         return obj

