
from django.urls import path
from .views import Reg
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('r/', Reg),
]
