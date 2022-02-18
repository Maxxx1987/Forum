from django.shortcuts import Http404
from apps.likes.forms import AddLikeForm
from django.views.generic.edit import CreateView


class LikeCreateView(CreateView):
    form_class = AddLikeForm

    def get(self, request, *args, **kwargs):
        raise Http404

    def get_success_url(self):
        return self.object.comment.get_absolute_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
