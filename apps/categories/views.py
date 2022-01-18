from django.shortcuts import render

from apps.categories.models import Category, Topic


def categories(request):
    context = {
        'category_list': Category.objects.all().order_by('name'),
    }
    return render(request, 'categories.html', context=context)


def topics(request, **kwargs):
    category_id = kwargs.get('id')
    context = {
        'category_id': category_id,
        'category_name': Category.objects.get(id=category_id).name,
        'topic_list': Topic.objects.filter(category=category_id).order_by('name'),
    }
    return render(request, 'topics.html', context=context)


