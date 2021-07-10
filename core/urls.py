
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('coresite.urls')),
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('carts/', include('carts.urls')),
    path('payment/', include('billings.urls')),
    path('mycourses/', include('enrolls.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('ratings/', include('star_ratings.urls', namespace='ratings')),
    path('admin/', include('customadmin.urls')),
    path('quiz/', include('quizapp.urls')),
    path('superadmin/', admin.site.urls),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = 'coresite.views.handler404'
handler500 = 'coresite.views.handler500'

admin.site.site_header = "GainSkill Super Admin"
admin.site.site_title = "GainSkill"
admin.site.index_title = "Welcome to GainSkill"