from rest_framework.serializers import ModelSerializer

from core.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'synopsis', 'genre', 'author', 'year', 'created_at', 'updated_at')
