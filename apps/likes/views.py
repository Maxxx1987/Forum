from django.shortcuts import Http404, redirect
from apps.likes.forms import AddLikeForm
from apps.likes.models import Like


def add_like(request, **kwargs):
    if request.method == 'POST':
        comment_id = kwargs.get('id')
        form = AddLikeForm(request.POST)
        if form.is_valid():
            like = Like.objects.filter(user=request.user, comment_id=comment_id).first()
            if not like:
                like = Like.objects.create(user=request.user, comment_id=comment_id)
            return redirect(f'/category/{like.comment.topic.category_id}/topic/{like.comment.topic_id}/comment/{comment_id}/')
    else:
        raise Http404
