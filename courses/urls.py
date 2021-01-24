from django.urls import path


from .views import CourseListView, SingleCourseView, CategoryListView,  create_course_with_lessons, SingleCategoryListView


app_name = "courses"

urlpatterns = [

    
    path('', CourseListView.as_view(), name="courses"),
    path('category/', CategoryListView.as_view(), name="category"),
    path('category/<int:id>/', SingleCategoryListView.as_view(), name="single-category"),
    path('create/', create_course_with_lessons, name="create-course"),
    path('course/<slug:slug>/', SingleCourseView.as_view(), name="single-course"),


]
