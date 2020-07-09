from django.db import models


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
    price = models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    offer_price =  models.DecimalField(max_digits=5, decimal_places=2,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    timestamp = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"
        db_table = "courses"

    def __str__(self):
        return self.title
    

class LessonContent(models.Model):
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
