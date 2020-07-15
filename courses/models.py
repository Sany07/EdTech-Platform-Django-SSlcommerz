from django.db import models
from django.dispatch import receiver
import os

class Category(models.Model):
    name = models.CharField(max_length=20)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        db_table = "categories"

    def __str__(self):
        return self.name
    

class Course(models.Model):
    title = models.CharField(max_length=250,blank=False)
    description = models.TextField()
    thumbnail = models.ImageField(upload_to='photos/course/%Y-%m-%d/')
    price = models.DecimalField(max_digits=100, decimal_places=2,null=True,blank=True)
    offer_price =  models.DecimalField(max_digits=100, decimal_places=2,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        db_table = "courses"

    def __str__(self):
        return self.title



@receiver(models.signals.post_delete, sender=Course)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.thumbnail:
        if os.path.isfile(instance.thumbnail.path):
            os.remove(instance.thumbnail.path)

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

    new_file = instance.thumbnail
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
    

class LessonContent(models.Model):
    title  = models.CharField(max_length=250, blank=True)
    video_link = models.URLField(blank=False)

    class Meta:
        verbose_name = "Lesson Content"
        verbose_name_plural = "Lessons Contents"
        db_table = "lessonsContents"

    def __str__(self):
        return self.video_link



class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course')
    title  = models.CharField(max_length=250, blank=False)
    video_link = models.ManyToManyField(LessonContent)
    # video_link = models.Ma(LessonContent, on_delete=models.CASCADE, related_name='lessoncontent')


    class Meta:
        verbose_name = "Lesson"
        verbose_name_plural = "Lessons"
        db_table = "lessons"

    def __str__(self):
        return self.title
