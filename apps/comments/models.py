from django.db import models

class Comment(models.Model):
    User = models.ForeignKey()
    Topic = models.IntegerField(default=0)
    Text = models.BooleanField(default=False)
    Create_dt = models.DateTimeField()
# Create your models here.
