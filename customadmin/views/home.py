from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required


# Create your models here.
from ..forms import *
from ..models import PaymentGatewaySettings
# Create your views here.
from accounts.models import CustomUser, Profile
from courses.models import *
from enrolls.models import EnrollCouese


class DashBoardView(TemplateView):

    template_name = 'adminsection/pages/index.html'

    @method_decorator(login_required(login_url=reverse_lazy('accounts:login')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_total_statistics(self):
        users = CustomUser.objects.all()
        totalusers = users.count()
        totalteachers = users.filter(role="tea").count()
        totalstudents = users.filter(role="stu").count()
        totalcourses = Course.objects.all().count()
        return totalusers, totalteachers, totalstudents, totalcourses

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        results = self.get_total_statistics()
        context["totalusers"] = results[0]
        context["totalteachers"] = results[1]
        context["totalstudents"] = results[2]
        context["totalcourses"] = results[3]
        
        print(self.request.path)
        return context

class customPostMethod():
    def post(self, request):

        form = self.form_class(request.POST or None , request.FILES or None)

        if form.is_valid():
            form = form.save(commit=False)
            form.save()
            messages.success(request,'Update Successfull')

class FrontEndSettings(UpdateView):
    model = FrontEndSettings
    form_class = GeneralSettingsForm
    context_object_name = 'frontend_settings'
    customPost = customPostMethod
    success_url = reverse_lazy('customadmin:frontend-settings')
    template_name = 'adminsection/pages/site-settings.html'


    @method_decorator(login_required(login_url=reverse_lazy('customadmin:login')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("Settings doesn't exists")
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = super().get_queryset().last()

        if obj is None:
            self.customPost.post(self, self.request)

        return obj





class PaymentGatewaySettingsView(UpdateView):
    model = PaymentGatewaySettings
    form_class = GatewayForm
    customPost = customPostMethod
    context_object_name = 'paymentgateway'
    success_url = reverse_lazy('customadmin:gateway-settings')
    template_name = 'adminsection/pages/payment-gateway-settings.html'

    @method_decorator(login_required(login_url=reverse_lazy('customadmin:login')))
    @method_decorator(staff_member_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(self.request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            raise Http404("Settings doesn't exists")
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = super().get_queryset().last()

        if obj is None:
            self.customPost.post(self, self.request)

        return obj

