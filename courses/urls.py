from django.urls import path


from .views import CourseListView, SingleCourseView, lesson_content, create_course_with_lessons


app_name = "courses"

urlpatterns = [

    
    path('', CourseListView.as_view(), name="courses"),
    path('create/', create_course_with_lessons, name="create-course"),
    path('course/<slug:slug>/', SingleCourseView.as_view(), name="single-course"),
    path('lesson/<int:id>/', lesson_content, name="lesson"),


]
