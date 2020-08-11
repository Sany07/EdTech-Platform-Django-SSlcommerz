from django.shortcuts import render, get_object_or_404, HttpResponseRedirect, redirect
from django.views.generic import ListView, DetailView
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.db.models import Count,Q
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from star_ratings.models import Rating , UserRating, AbstractBaseRating
from django.contrib.contenttypes.models import ContentType


from django.views.generic.edit import FormMixin


from .models import *
from .forms import *
from .decorators import user_is_instructor

from accounts.models import CustomUser
from carts.models import Cart
from reviews.models import Review
from reviews.forms import ReviewForm

class CourseListView(ListView):
    model = Course
    context_object_name = 'courses'
    paginate_by = 6
    template_name = "courses/courses.html"

    def get_queryset(self):
        return self.model.objects.order_by('-id')

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart_obj'] = cart_obj
        # context['enrolled'] = EnrolledList(self.request)
        
        return context
    

class SingleCourseView(FormMixin, DetailView):
    model = Course
    context_object_name = 'course'
    form_class = ReviewForm
    template_name = "courses/single-courses.html"

    
    @xframe_options_sameorigin
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


    def get_similar_category_courses(self):      
        return self.model.objects.filter(category=self.object.category).order_by("-id")[:5]

    def get_total_lecture(self):               
        return Lesson.objects.filter(course=self.object.id).values('video_link').count()
        
    def get_reviews(self):       
        return Review.objects.filter_by_course(self.object).order_by("-id")   
        
    def get_c_t(self):            
        return ContentType.objects.get(model='course')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_lecture'] = self.get_total_lecture()
        context['similar_category_courses'] = self.get_similar_category_courses()
        context['reviews'] = self.get_reviews()
        context['form'] = self.get_form()


        return context



@login_required
@user_is_instructor
def create_course_with_lessons(request):
    courseform = CourseModelForm(request.POST or None)
    formset = LessonFormset(queryset=Lesson.objects.none())
    ContentFormset = LessonContentFormset(queryset=LessonContent.objects.none())
    
    if request.method == 'POST':

        courseform = CourseModelForm(request.POST or None , request.FILES or None)
        formset = LessonFormset(request.POST)
        ContentFormset = LessonContentFormset(request.POST)
        user = get_object_or_404(CustomUser, id=request.user.id)
        
        if courseform.is_valid and formset.is_valid() and ContentFormset.is_valid():
            categories = Category.objects.get(id=1) 
            course  = courseform.save(commit=False)
            course.instructor = user
            course.save()
            

            for form in formset:
                lesson = form.save(commit=False)
                if lesson.curriculum_title != '':
                    lesson.course = course
                    lesson.save()

                    for form in ContentFormset:
                        lessoncontent = form.save(commit=False)
                        if lessoncontent.title != '':
                            lessoncontent.save()

                            lesson.video_link.add(lessoncontent)
                    # break
            return redirect(reverse("courses:single-course", kwargs={
                                'slug': course.slug
                                }))

    categories = Category.objects.all()   
    return render(request, 'courses/create-course.html', {
        'courseform': courseform,
        'formset': formset,
        'ContentFormset':ContentFormset,
        'categories':categories

    })



