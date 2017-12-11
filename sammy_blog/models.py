from django.db import models
from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=140)
    date = models.DateField(blank=True, null=True)
    content = HTMLField(blank=True, null=True)

    def __str__(self):
        return self.title
