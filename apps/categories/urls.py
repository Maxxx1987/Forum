from django.urls import path

from apps.comments.views import (
    CommentCreateView,
    CommentListView,
    CommentDetailView,
    CommentDeleteView,
    CommentUpdateView
)
from apps.categories.views import CategoryListView, TopicCreateView, TopicListView
from apps.likes.views import LikeCreateView

urlpatterns = [
    path('', CategoryListView.as_view()),

    path('<slug:slug>/', TopicListView.as_view()),
    path('<int:id>/topic/add/', TopicCreateView.as_view()),

    path('<int:cat_id>/topic/<int:id>/', CommentListView.as_view()),
    path('<int:cat_id>/topic/<int:id>/comment/add/', CommentCreateView.as_view()),
    path('<int:cat_id>/topic/<int:topic_id>/comment/<int:id>/', CommentDetailView.as_view()),
    path('<int:cat_id>/topic/<int:topic_id>/comment/<int:id>/update/', CommentUpdateView.as_view()),
    path('<int:cat_id>/topic/<int:topic_id>/comment/<int:id>/delete/', CommentDeleteView.as_view()),

    path('<int:cat_id>/topic/<int:topic_id>/comment/<int:id>/like/add/', LikeCreateView.as_view()),
]
