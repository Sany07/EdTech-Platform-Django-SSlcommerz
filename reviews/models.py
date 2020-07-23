from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType 

User= settings.AUTH_USER_MODEL


from .manager import CommentManager


class Review(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    def __str__(self):
        return self.user.username        
    

    class Meta:
        verbose_name = "Course Review"
        verbose_name_plural = "Courses Reviews"
        db_table = "courseReview"

    def __str__(self):
        return self.user.username