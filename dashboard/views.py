from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from enrolls.models import EnrollCouese


class MyCourseListView(ListView):
    model = EnrollCouese
    context_object_name = 'mycourses'
    template_name = "site/my-courses.html"

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    

    def get_queryset(self):
        return self.model.objects.filter(user = self.request.user).first()
    






