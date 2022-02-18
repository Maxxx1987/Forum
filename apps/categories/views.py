from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from apps.categories.models import Category, Topic
from apps.categories.forms import AddTopicForm


class CategoryListView(ListView):
    model = Category
    ordering = ('name',)
    template_name = 'categories.html'


class TopicListView(ListView):
    model = Topic
    ordering = ('-created_at', '-id')
    template_name = 'topics.html'

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class TopicCreateView(CreateView):
    form_class = AddTopicForm
    template_name = 'add_topic.html'

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.category_id = int(self.kwargs['id'])
        return super().form_valid(form)
