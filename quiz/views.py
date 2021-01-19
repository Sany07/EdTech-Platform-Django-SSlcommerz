from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse

from .forms import QuizQuestionForm, QuizForm
from .models import *



def AddQuiz(request):
    template_name = 'mainsite/quiz/add_quiz.html'
    
    form = QuizForm(request.POST or None , request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            # first save this book, as its reference will be used in `Author`
            form  = form.save(commit=False)
            form.save()
            return redirect(reverse("quiz:add_quiz_question", kwargs={
                'id': form.id
                }))
    return render(request, template_name, {
        'form': form,
    })

def AddQuizQuestion(request,id):
    response_data = {}
    success_status = 'success'
    success_msg = 'Question Added'
    error_status = 'error'
    error_msg = 'Somthing went wrong. Please Try Again'
    template_name = 'mainsite/quiz/add_quiz_question.html'
    quiz_id = get_object_or_404(Quiz, id=id)
    form = QuizQuestionForm(request.POST or None , request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            # first save this book, as its reference will be used in `Author`
            form  = form.save(commit=False)
            print(quiz_id.id)
            print(quiz_id)
            form.quiz__Quiz = quiz_id.id
            form.save()

            if request.is_ajax():
                response_data['status'] = success_status
                response_data['msg'] = success_msg

            else:
                response_data['status'] = 'error_status' 
                response_data['msg'] = form.errors
            return JsonResponse(response_data, safe=False)
            #return redirect ('/')
    return render(request, template_name, {
        'form': form,
        'quiz':quiz_id
    })
