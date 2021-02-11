import os
from django.db import models
from django.dispatch import receiver
from django.shortcuts import reverse
from django.utils.text import slugify
from django.db.models.signals import pre_save, post_save
from django.contrib.contenttypes.fields import GenericRelation
from django.contrib.contenttypes.models import ContentType 
from django.conf import settings

User = settings.AUTH_USER_MODEL

from courses.utils import unique_slug_generator
from star_ratings.models import Rating
from reviews.models import Review


class Category(models.Model):
    name = models.CharField(max_length=20)
    # slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True, null=True ,on_delete=models.CASCADE, related_name='children')

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("courses:single-category", kwargs={'id': self.id})

    def get_course_count_by_category(self):
        enroll_count= self.category.values('category__id').aggregate(models.Count('category__id'))
        return enroll_count['category__id__count']    

class Course(models.Model):
    title = models.CharField(max_length=250,blank=False)
    slug = models.SlugField(unique=True, max_length=255)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='photos/course/%Y-%m-%d/')
    price = models.DecimalField(max_digits=65, decimal_places=2,null=True,blank=True)
    offer_price =  models.DecimalField(max_digits=65, decimal_places=2,null=True,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    # language = models.CharField(max_length=50)
    ratings = GenericRelation(Rating, related_query_name='ratings')
    is_published = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    instructor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='instructor')


    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        db_table = "courses"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:single-course", kwargs={'slug': self.slug})

    @property
    def lesson(self):
        return self.lesson_set.all()
        
    @property
    def get_content_type(self):
        content_type = ContentType.objects.get_for_model(self.__class__)
        return content_type    

    @property
    def get_enroll_count(self):
        # comment_count = Course.objects.all().annotate(Count('products__id')).order_by('-products__id') 
        enroll_count= self.products.values('products__id').aggregate(models.Count('products__id'))
        return enroll_count['products__id__count']

def rl_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(rl_pre_save_receiver, sender=Course)
  
  

@receiver(models.signals.post_delete, sender=Course)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.thumbnail:
        #for local server
        
        # if os.path.isfile(instance.thumbnail.path):
        #     os.remove(instance.thumbnail.path)
        
        #for aws s3
        instance.thumbnail.delete(save=False)
            


@receiver(models.signals.pre_save, sender=Course)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = sender.objects.get(pk=instance.pk).thumbnail
    except sender.DoesNotExist:
        return False

    #for local server
    new_file = instance.thumbnail
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    
    #for aws s3
    # new_avatar = instance.thumbnail
    # if old_file and old_file.url != new_avatar.url:
    #     old_file.delete(save=False)




class LessonContent(models.Model):
    title  = models.CharField(max_length=250, blank=False)
    video_link = models.URLField(max_length=500, blank=True, null=True)
    text_content = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name = "Lesson Content"
        verbose_name_plural = "Lessons Contents"
        db_table = "lessonsContents"

    def __str__(self):
        return self.title



class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    curriculum_title  = models.CharField(max_length=250, blank=False)
    video_link = models.ManyToManyField(LessonContent)
    # video_link = models.ForeignKey(LessonContent, on_delete=models.CASCADE, related_name='lessoncontent')


    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        db_table = "lessons"

    def __str__(self):
        return self.curriculum_title

    @property
    def lesson(self):
        return self.lessoncontent_set.all()