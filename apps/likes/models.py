from django.conf import settings
from django.db import models

from apps.comments.models import Comment


class Like(models.Model):
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    comment = models.ForeignKey(Comment, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
