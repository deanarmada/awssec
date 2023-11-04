from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField()
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField()
    timestamp = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-id']
