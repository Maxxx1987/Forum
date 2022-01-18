"""apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from apps.comments.views import comments, add_comment, comment
from apps.categories.views import categories, topics
from apps.likes.views import add_like


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', categories),
    re_path(r'^category/(?P<id>\d+)/$', topics),
    re_path(r'^category/(?P<cat_id>\d+)/topic/(?P<id>\d+)/$', comments),

    re_path(r'^category/(?P<cat_id>\d+)/topic/(?P<id>\w+)/comment/add/$', add_comment),
    re_path(r'^category/(?P<cat_id>\d+)/topic/(?P<topic_id>\w+)/comment/(?P<id>\w+)/$', comment),
    re_path(r'^category/(?P<cat_id>\d+)/topic/(?P<topic_id>\d+)/comment/(?P<id>\d+)/like/add/$', add_like)

]
