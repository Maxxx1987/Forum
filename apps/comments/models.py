from django.db import models
from django.conf import settings

from apps.categories.models import Topic


class Comment(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return f'/category/{self.topic.category_id}/topic/{self.topic_id}/'
