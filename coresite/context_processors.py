from courses.models import Category
from customadmin.models import FrontEndSettings

def categories_context_processor(request):
    categories = Category.objects.all()

    return {'categories': categories}

def site_context_processor(request):
    site_data = FrontEndSettings.objects.last()

    return {'site_data':site_data}