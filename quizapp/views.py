from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.contrib import messages

from .forms import QuizQuestionForm, QuizForm , QuizExamForm
from .models import *



def AddQuiz(request, id):
    template_name = 'mainsite/quiz/add_quiz.html'
    
    form = QuizForm(request.POST or None , request.FILES or None)
    if request.method == 'POST':
        if form.is_valid():
            courseid = get_object_or_404(Course, id= id)
            # first save this book, as its reference will be used in `Author`
            form  = form.save(commit=False)
            form.course = courseid
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

submitans = []
anslist = []


def Exam(request, id):
    answers = QuizQuestion.objects.filter(quiz = id).order_by('-id')
    if len(anslist) == 0:
        print('a')        
        for i in answers:
            anslist.append(i.ans)
    
    count = answers.count()
    paginator = Paginator(answers,1)
    try:
        page = int(request.GET.get('page','1'))  
    except:
        page =1
    try:
        questions = paginator.page(page)
    except(EmptyPage,InvalidPage):

        questions=paginator.page(paginator.num_pages)
    
    return render(request,'mainsite/quiz/quiz_exam.html',{'QuizExamForm':QuizExamForm, 'obj':answers,'questions':questions,'count':count, 'id':id})

def result(request, id):
    score =0
    obj = QuizExam.objects.filter(quiz = id, user = request.user.id).order_by('-id')
    
    for o in obj:
        submitans.append(o.ans)
    print(submitans)
    for i in range(len(anslist)):
        print(i)
        if anslist[i]==submitans[i]:
            score +=1
            print(submitans[i])
    # print(score)
    anslist.clear()
    submitans.clear()

    return render(request,'mainsite/quiz/result.html',{'score':score,'lst':submitans})

def save_ans(request):
    response_data = {}
    success_status = 'success'
    success_msg = 'Ans Submitted'
    error_status = 'error'
    error_msg = 'Somthing went wrong. Please Try Again'

    if request.method =='POST':
        form = QuizExamForm(request.POST)
        if form.is_valid():
            is_success = form.save()
            if is_success and request.is_ajax():
                response_data['status'] = success_status
                response_data['msg'] = success_msg

            elif is_success:    
                messages.success(request, success_msg)

            else:
                response_data['status'] = error_status 
                response_data['msg'] = form.errors
            return JsonResponse(response_data, safe=False)

        else:
            response_data['status'] = error_status 
            response_data['msg'] = error_msg
            return JsonResponse(response_data, safe=False)

    return redirect('/')

def clr(request):
    lst.clear()
    anslist.clear()
    return redirect('quiz:exam')

