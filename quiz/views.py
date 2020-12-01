from django.shortcuts import render, redirect
from django.views import generic

from .forms import BookModelForm

from .models import *



def QuizAdd(request):
    template_name = 'mainsite/quiz/add_quiz.html'
    if request.method == 'GET':
        bookform = BookModelForm(request.GET or None)
    elif request.method == 'POST':
        bookform = BookModelForm(request.POST)
        if bookform.is_valid():
            # first save this book, as its reference will be used in `Author`
            book = bookform.save()
            for form in formset:
                # so that `book` instance can be attached.
                author = form.save(commit=False)
                author.book = book
                author.save()
            return '/'
    return render(request, template_name, {
        'bookform': bookform,
    })
