from django.contrib import messages, auth
from django.shortcuts import render , redirect , HttpResponseRedirect, get_object_or_404
from django.views.generic import CreateView, DetailView, RedirectView, View , ListView, TemplateView, FormView
from django.urls import reverse, reverse_lazy

from accounts.models import *
from accounts.forms import *

class InstructorRegisterView(CreateView):
    """
        Provides the ability to Register as a Instructor
    """
    model = CustomUser
    form_class = TeacherRegistrationForm
    template_name = "mainsite/accounts/instructor-register.html"


    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('coresite:home')
        return super().dispatch(self.request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request,'Registration Successfull')
            return redirect('accounts:login')
        else:
            context={
                'form':form
            }
            return render(request, self.template_name ,context)

class StudentRegisterView(CreateView):
    """
        Provides the ability to Register as a Student
    """
    model = CustomUser
    form_class = StudentRegistrationForm
    template_name = "mainsite/accounts/student-register.html"


    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('coresite:home')
        return super().dispatch(self.request, *args, **kwargs)


    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request,'Registration Successfull')
            return redirect('accounts:login')
        else:
            context={
                'form':form
            }
            return render(request, self.template_name ,context)


class LogInView(FormView):
    """
        Provides the ability to login as a user with an email/username and password
    """
    success_url = '/'
    form_class = UserLoginForm
    template_name = 'mainsite/accounts/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return HttpResponseRedirect(self.get_success_url())
        return super().dispatch(self.request, *args, **kwargs)

    def get_success_url(self):
        if 'next' in self.request.GET and self.request.GET['next'] != '':
            return self.request.GET['next']
        else:
            return self.success_url

    def get_form_class(self):
        return self.form_class

    def form_valid(self, form):
        auth.login(self.request, form.get_user())
        messages.success(self.request, 'You are Successfully logged In')
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        """If the form is invalid, render the invalid form."""
        messages.error(self.request, 'Login Faild ! Try Again')
        
        return self.render_to_response(self.get_context_data(form=form))    


class LogoutView(RedirectView):
    """
    Provides users the ability to logout
    """
    url = '/accounts/login'

    def get(self, request, *args, **kwargs):
        auth.logout(request)
        messages.success(self.request, 'You are Successfully logged Out')
        return super(LogoutView, self).get(request, *args, **kwargs)


class ProfileView(DetailView):
    model = CustomUser
    context_object_name = 'profile'
    pk_url_kwarg = 'id'
    template_name = 'mainsite/accounts/profile.html'


    def get_course(self):               
        return Course.objects.filter(instructor=self.object.id)
        # return Lesson.objects.filter(course=self.object.id).values('video_link').count()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_courses'] = self.get_course()
        context['total'] = self.get_course().count()

        return context



