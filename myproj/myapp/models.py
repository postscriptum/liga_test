from django.db import models
from django.contrib.auth.models import User


class Source(models.Model):
    sid = models.SlugField()
    name = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.sid


class Document(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    url = models.URLField()
    created = models.DateTimeField()
    source = models.ForeignKey(Source, on_delete=models.CASCADE)
    added = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    edit_count = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title
