from django.template.loader import get_template
from django.http import HttpResponse, JsonResponse

from apps.categories.models import Category, Topic
from apps.comments.models import Comment


def comments(request, **kwargs):
    category_id = kwargs.get('cat_id')
    topic_id = kwargs.get('id')
    template = get_template('comments.html')
    context = {
        'topic_name': Topic.objects.get(id=topic_id, category=category_id).name,
        'comment_list': (Comment.objects
                         .filter(topic=topic_id,
                                 topic__category=category_id)
                         .order_by('create_at')),
    }
    return HttpResponse(template.render(context=context))
