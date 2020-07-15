from django.shortcuts import render , redirect

from django.shortcuts import render
from django.views.generic import View , ListView, TemplateView, FormView




from courses.models import *


from accounts.forms import *

def create_book_with_authors(request):
    courseform = CourseModelForm(request.POST or None)
    formset = LessonFormset(queryset=Lesson.objects.none())
    ContentFormset = LessonContentFormset(queryset=LessonContent.objects.none())
    
    if request.method == 'POST':

        courseform = CourseModelForm(request.POST or None , request.FILES or None)
        formset = LessonFormset(request.POST)
        ContentFormset = LessonContentFormset(request.POST)
        
        if courseform.is_valid and formset.is_valid() and ContentFormset.is_valid():
            categories = Category.objects.get(id=1) 
            course  = courseform.save(commit=False)
            # course.category=categories
            course.save()
            
            
            for form in ContentFormset:
                lesson = form.save(commit=False)         
                lesson.save()
            for form in formset:
                author = form.save(commit=False)
                author.course = course
                author.save()
                author.video_link.add(lesson)
                
    categories = Category.objects.all()   
    return render(request, 'courses/create-course.html', {
        'courseform': courseform,
        'formset': formset,
        'ContentFormset':ContentFormset,
        'categories':categories

    })



