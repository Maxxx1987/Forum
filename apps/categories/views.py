from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from apps.categories.models import Category, Topic
from apps.categories.forms import AddTopicForm


class CategoryView(ListView):
    model = Category
    ordering = ('name',)
    template_name = 'categories.html'


class TopicView(ListView):
    model = Topic
    ordering = ('-created_at', '-id')
    template_name = 'topics.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category_id=self.kwargs['id'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['category'] = Category.objects.get(id=int(self.kwargs['id']))
        return context


class AddTopicView(CreateView):
    form_class = AddTopicForm
    success_url = '/category/{category_id}/'
    template_name = 'add_topic.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.category_id = int(self.kwargs['id'])
        return super().form_valid(form)
