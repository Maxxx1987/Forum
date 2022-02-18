from django.db import models
from django.conf import settings
from django.core.validators import MinLengthValidator

from apps.categories.models import Topic


class Comment(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    text = models.TextField(validators=[MinLengthValidator(3)])
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if len(self.text) > 50:
            return f'{self.text[:47]}...'
        return self.text

    def get_absolute_url(self):
        return f'/category/{self.topic.category_id}/topic/{self.topic_id}/comment/{self.id}/'
