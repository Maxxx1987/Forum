from django.shortcuts import render, redirect

from apps.categories.models import Category, Topic
from apps.categories.forms import AddTopicForm


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

def add_topic(request, **kwargs):
    category_id = kwargs.get('id')

    if request.method == 'POST':
        # создание топика
        topic_form = AddTopicForm(request.POST)
        if topic_form.is_valid():
            name = topic_form.cleaned_data['name']
            description = topic_form.cleaned_data['description']
            Topic.objects.create(user=request.user, name=name, description=description, category_id=category_id)
            return redirect(f'/category/{category_id}/')
        else:
            pass

    topic_form = AddTopicForm()
    context = {
        'form': topic_form,
        'cat_id': category_id,
    }
    return render(request, 'add_topic.html', context=context)
