from django.db import models
from django.conf import settings
User = settings.AUTH_USER_MODEL


# Create your models here.
from courses.models import Course

QUIZ_CHOICES =( 

    ("choice_one", "One"), 
    ("choice_two", "Two"), 
    ("choice_three", "Three"), 
    ("choice_four", "Four"), 

) 
class Quiz(models.Model):
    
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courseref')
    descriptions = models.CharField(max_length=250,blank=False)


    class Meta:
        verbose_name = "Quiz"
        verbose_name_plural = "Quizzes"
        db_table = "quiz"

    def __str__(self):
        return self.descriptions


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz')
    question = models.CharField(max_length=250,blank=True, null=True)
    image    = models.ImageField(upload_to='photos/quiz/%Y-%m-%d/', blank=True, null=True)
    choice_one = models.CharField(max_length=250,blank=False)
    choice_two = models.CharField(max_length=250,blank=False)
    choice_three = models.CharField(max_length=250,blank=False)
    choice_four =  models.CharField(max_length=250,blank=False)
    ans = models.CharField(max_length=12,choices = QUIZ_CHOICES) 

    class Meta:
        verbose_name = "QuizQuestion"
        verbose_name_plural = "QuizQuestions"
        db_table = "quizquestion"
    def __str__(self):
        return self.question




class QuizResult(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz_name')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='user')
    marks = models.IntegerField()

    class Meta:
        verbose_name = "Result"
        verbose_name_plural = "Results"
        db_table = "quizresult"


    def __str__(self):
        return self.user.username


class QuizExam(models.Model):
    question = models.ForeignKey(QuizQuestion, on_delete=models.CASCADE, related_name='question_exam')
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='exam_user')
    ans = models.CharField(max_length=12,choices = QUIZ_CHOICES) 

    class Meta:
        verbose_name = "Exam"
        verbose_name_plural = "Exams"
        db_table = "Exam"


    def __str__(self):
        return self.user.username
