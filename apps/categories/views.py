from django.template.loader import get_template
from django.http import HttpResponse, JsonResponse

from apps.categories.models import Category, Topic


def categories(request):
    template = get_template('categories.html')
    context = {
        'category_list': Category.objects.all().order_by('name'),
    }
    return HttpResponse(template.render(context=context))


def topics(request, **kwargs):
    category_id = kwargs.get('id')
    template = get_template('topics.html')
    context = {
        'category_id': category_id,
        'category_name': Category.objects.get(id=category_id).name,
        'topic_list': Topic.objects.filter(category=category_id).order_by('name'),
    }
    return HttpResponse(template.render(context=context))


