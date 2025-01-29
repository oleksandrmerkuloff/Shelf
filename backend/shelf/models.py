from django.db import models


class Tag(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Book(models.Model):
    title = models.CharField(max_length=150)
    file = models.FileField()
    description = models.TextField(blank=True, null=True)
    language = models.CharField(max_length=30, default='other')
    author = models.CharField(max_length=150, default='Unknown')
    added_date = models.DateField(auto_now_add=True)
    tags = models.ManyToManyRel(Tag)

    def __str__(self):
        return self.title
