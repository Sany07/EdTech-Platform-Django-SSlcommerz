from django.db import models
from django.contrib.contenttypes.models import ContentType 

class CommentManager(models.Manager):
    def filter_by_course(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        object_id = instance.id
        review = super(CommentManager, self).filter(content_type=content_type, object_id = object_id )
        return review