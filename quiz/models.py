from django.db import models

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

    def __str__(self):
        return self.descriptions


class QuizQuestion(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz')
    question = models.CharField(max_length=250,blank=False)
    image    = models.ImageField(upload_to='photos/quiz/%Y-%m-%d/', blank=True, null=True)
    choice_one = models.CharField(max_length=250,blank=False)
    choice_two = models.CharField(max_length=250,blank=False)
    choice_three = models.CharField(max_length=250,blank=False)
    choice_four =  models.CharField(max_length=250,blank=False)
    ans = models.CharField(max_length=300,choices = QUIZ_CHOICES) 

    class Meta:
        verbose_name = "QuizQuestion"
        verbose_name_plural = "QuizQuestions"

    def __str__(self):
        return self.question


class QuizParticipent(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='quiz')
    question = models.CharField(max_length=250,blank=False)
    image    = models.ImageField(upload_to='photos/quiz/%Y-%m-%d/', blank=True, null=True)
    choice_one = models.CharField(max_length=250,blank=False)
    choice_two = models.CharField(max_length=250,blank=False)
    choice_three = models.CharField(max_length=250,blank=False)
    choice_four =  models.CharField(max_length=250,blank=False)
    ans = models.CharField(max_length=300,choices = QUIZ_CHOICES) 

    class Meta:
        verbose_name = "QuizQuestion"
        verbose_name_plural = "QuizQuestions"

    def __str__(self):
        return self.question


