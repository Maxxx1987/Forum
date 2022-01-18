from django.shortcuts import render

from apps.categories.models import Topic
from apps.comments.models import Comment


def comments(request, **kwargs):
    category_id = kwargs.get('cat_id')
    topic_id = kwargs.get('id')
    topic = Topic.objects.get(id=topic_id, category=category_id)
    context = {
        'topic': topic,
        'comment_list': (Comment.objects
                         .filter(topic=topic_id)
                         .order_by('create_at')),
    }
    return render(request, 'comments.html', context=context)
