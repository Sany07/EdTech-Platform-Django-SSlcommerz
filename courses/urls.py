from django.urls import path


from .views import CourseListView, SingleCourseView, lesson_content


app_name = "courses"

urlpatterns = [

    
    path('', CourseListView.as_view(), name="courses"),
    path('course/<slug:slug>/', SingleCourseView.as_view(), name="single-course"),
    path('lesson/<int:id>/', lesson_content, name="lesson"),


]
