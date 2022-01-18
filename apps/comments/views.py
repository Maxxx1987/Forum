from django.shortcuts import render, redirect

from apps.categories.models import Topic
from apps.comments.models import Comment
from apps.comments.forms import AddCommentForm
from apps.likes.forms import AddLikeForm
from apps.likes.models import Like


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


def add_comment(request, **kwargs):
    category_id = kwargs.get('cat_id')
    topic_id = kwargs.get('id')

    if request.method == 'POST':
        # создание коммента
        comment_form = AddCommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.cleaned_data['comment']
            Comment.objects.create(user=request.user, topic_id=int(topic_id), text=comment)
            return redirect(f'/category/{category_id}/topic/{topic_id}/')
        else:
            pass

    comment_form = AddCommentForm()
    context = {
        'category_id': category_id,
        'topic_id': topic_id,
        'form': comment_form,
    }
    return render(request, 'add_comment.html', context=context)


def comment(request, **kwargs):
    # category_id = kwargs.get('cat_id')
    # topic_id = kwargs.get('topic_id')
    comment_id = kwargs.get('id')
    # topic = Topic.objects.get(id=topic_id, category=category_id)
    context = {
        # 'topic': topic,
        'comment': Comment.objects.get(id=comment_id),
        'like_count': Like.objects.filter(comment_id=comment_id).count(),
        'like_form': AddLikeForm(),
    }
    return render(request, 'comment.html', context=context)
