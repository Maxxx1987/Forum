from django.conf import settings
from django.db import models

from autoslug import AutoSlugField


class Category(models.Model):
    name = models.TextField()
    slug = AutoSlugField(populate_from='name', allow_unicode=True, null=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/category/{self.slug}/'


class Topic(models.Model):
    name = models.CharField('Название', max_length=255)
    description = models.TextField(null=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        pass

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/category/{self.category_id}/topic/{self.id}/'
