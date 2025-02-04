from rest_framework import serializers

from . import models


class BookSerializer(serializers.ModelSerializer):
    owner = serializers.StringRelatedField()
    tags = serializers.StringRelatedField(many=True)

    class Meta:
        model = models.Book
        fields = ['title', 'file', 'description', 'language', 'author', 'added_date', 'likes', 'dislikes', 'owner', 'tags']