from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField()
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=20, default='Undefined')
    author = models.CharField(max_length=150, default='Undefined')
    added_date = models.DateField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              related_name='books')
    tags = models.ManyToManyRel(Tag, related_name='books')

    def __str__(self):
        return self.title
