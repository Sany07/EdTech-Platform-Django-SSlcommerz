import string
from django.utils.text import slugify

def unique_slug_generator(instance, new_slug=None):
    """
    This is for a Django project and it assumes your instance 
    has a model with a slug field and a title character (char) field.
    """
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)

    Klass = instance.__class__
    qs = Klass.objects.filter(slug=slug)
 
    if qs:
        new_slug = "{slug}-{id}".format(
            slug=slug,
            id=qs.first().id
        )
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug