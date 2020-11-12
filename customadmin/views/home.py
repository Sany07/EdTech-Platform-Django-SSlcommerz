from django.shortcuts import render, redirect
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

        return context



class FrontEndSettings(UpdateView):
    pass
#     model = FrontEndSettings
#     form_class = FrontEndSettingsForm
#     context_object_name = 'frontend'
#     success_url = reverse_lazy('customadmin:frontend-settings')
#     template_name = 'adminsection/pages/site-settings.html'


#     @method_decorator(login_required(login_url=reverse_lazy('customadmin:login')))
#     @method_decorator(staff_member_required)
#     def dispatch(self, request, *args, **kwargs):
#         return super().dispatch(self.request, *args, **kwargs)


#     def get(self, request, *args, **kwargs):
#         try:
#             self.object = self.get_queryset().last()
#         except Http404:
#             raise Http404("Data doesn't exists")

#         return self.render_to_response(self.get_context_data())


class custompostmethod():
    def post(self, request):

        form = self.form_class(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.save()


class PaymentGatewaySettingsView(UpdateView):
    model = PaymentGatewaySettings
    form_class = GatewayForm
    ss = custompostmethod
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
            raise Http404("User doesn't exists")
        return self.render_to_response(self.get_context_data())

    def get_object(self, queryset=None):
        obj = super().get_queryset().last()

        if obj is None:
            self.ss.post(self, self.request)

        return obj

