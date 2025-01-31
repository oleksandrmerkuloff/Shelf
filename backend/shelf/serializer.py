from rest_framework import serializers

import models


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Book
        fields = ['title', 'file', 'description', 'language', 'author', 'added_date', 'tags']
