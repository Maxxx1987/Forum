from apps.categories.models import Topic
from apps.comments.models import Comment
from apps.comments.forms import AddCommentForm
from apps.likes.forms import AddLikeForm
from apps.likes.models import Like
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.detail import DetailView


class CommentListView(ListView):
    model = Comment
    ordering = ('-create_at',)

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(topic_id=self.kwargs['id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['topic'] = Topic.objects.get(id=int(self.kwargs['id']))
        return context


class CommentDetailView(DetailView):
    model = Comment
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['like_count'] = Like.objects.filter(comment_id=self.object.id).count()
        context['like_form'] = AddLikeForm(initial={'comment': self.kwargs['id']})
        return context


class CommentCreateView(CreateView):
    form_class = AddCommentForm
    template_name = 'add_comment.html'

    def get_initial(self):
        return {'topic': self.kwargs['id']}

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['topic'] = Topic.objects.get(id=int(self.kwargs['id']))
        return context


class CommentUpdateView(UpdateView):
    form_class = AddCommentForm
    model = Comment
    pk_url_kwarg = 'id'


class CommentDeleteView(DeleteView):
    model = Comment
    pk_url_kwarg = 'id'

    def get_success_url(self):
        return self.object.topic.get_absolute_url()
