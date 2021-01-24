from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.core.paginator import Paginator

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
    success_msg = 'Question Added.'
    error_status = 'error'
    error_msg = 'Somthing went wrong. Please Try Again'
    template_name = 'mainsite/quiz/add_quiz_question.html'
    quiz = get_object_or_404(Quiz, id=id)
    form = QuizQuestionForm(request.POST or None , request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            # first save this book, as its reference will be used in `Author`
            form  = form.save(commit=False)
            # form.quiz__Quiz = quiz_id.id
            form.save()

            if request.is_ajax():
                response_data['status'] = success_status
                response_data['msg'] = success_msg
                
                return JsonResponse(response_data, safe=False)

            else:
                response_data['status'] = error_status 
                response_data['msg'] = form.errors
            #   return redirect ('/')
    return render(request, template_name, {
        'form': form,
        'quiz':quiz
    })

lst = []
anslist = []


def Exam(request):
    # print(lst)
    # print(anslist)
    # print(len(anslist))

    if len(anslist) == 0:
        print('a')

        answers = QuizQuestion.objects.all()
        for i in answers:
            print(i)
            anslist.append(i.ans)
    # print(anslist)
    obj = QuizQuestion.objects.all()
    count = QuizQuestion.objects.all().count()
    paginator = Paginator(obj,1)
    try:
        page = int(request.GET.get('page','1'))  
    except:
        page =1
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):

        questions=paginator.page(paginator.num_pages)
    
    return render(request,'mainsite/quiz/quiz_exam.html',{'obj':obj,'questions':questions,'count':count})

def result(request):
    print('lst')
    print(lst)
    print(anslist)
    score =0
    for i in range(len(lst)):
        if lst[i]==anslist[i]:
            
            score +=1
    print(score)
    lst.clear()
    
    return render(request,'mainsite/quiz/result.html',{'score':score,'lst':lst})

def save_ans(request):
    ans = request.GET['ans']
    print(ans)
    lst.append(ans)

def clr(request):
    lst.clear()
    anslist.clear()
    return redirect('quiz:exam')

