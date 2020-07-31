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

        cart_obj, new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj

        return context

    def post(self, request, *args, **kwargs):

        """Check Operation If the form is valid or invalid."""

        reviewform = self.get_form()
        if reviewform.is_valid():            
           return self.form_valid(reviewform)

        else:
            return self.form_invalid(reviewform)    

    def form_valid(self, reviewform):

        """If the form is valid, start save operation."""

        form= reviewform.save(commit = False)
        form.user = self.request.user
        form.content_type = self.get_c_t()
        form.save()           
        return HttpResponseRedirect("/")

    def form_invalid(self, form):

        """If the form is invalid, render the invalid form."""

        return self.render_to_response(self.get_context_data(form=form))



def lesson_content(request,id):

   data= get_object_or_404(Course, id=id)
   print(data)
   context={
       'data':data
   }
   return render(request,'courses/single-courses.html', context)

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
            
            for form in ContentFormset:
                lesson = form.save(commit=False)   
                    
                lesson.save()
            for form in formset:
                author = form.save(commit=False)
                author.course = course
                author.save()
                author.video_link.add(lesson)
                
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



