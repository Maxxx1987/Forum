from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic.base import TemplateView
from django.db.models import Count

from apps.categories.models import Category, Topic
from apps.categories.forms import AddTopicForm


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        data = []
        category_list = Category.objects.order_by('-created_at')[:3]
        for category in category_list:
            category_obj = {
                'category': category,
                'topic_list': (
                    Topic.objects
                    .filter(category=category)
                    .annotate(like_count=Count('comment__like'))
                    .order_by('-like_count', '-created_at')
                )[:2]
            }
            data.append(category_obj)
        context['data'] = data
        return context


class CategoryListView(ListView):
    model = Category
    ordering = ('name',)
    paginate_by = 3


class TopicListView(ListView):
    model = Topic
    ordering = ('-created_at', '-id')
    paginate_by = 4

    def get_queryset(self):
        qs = super().get_queryset()
        return qs.filter(category__slug=self.kwargs['slug'])

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['category'] = Category.objects.get(slug=self.kwargs['slug'])
        return context


class TopicCreateView(CreateView):
    model = Topic
    form_class = AddTopicForm
    template_name_suffix = '_create'

    def get_success_url(self):
        return self.object.get_absolute_url()

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.category_id = int(self.kwargs['id'])
        return super().form_valid(form)
