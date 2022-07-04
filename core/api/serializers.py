from rest_framework.serializers import ModelSerializer

from core.models import Book, Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name']


class BookSerializer(ModelSerializer):
    author = AuthorSerializer(
        read_only=True
    )

    class Meta:
        model = Book
        fields = ('id', 'title', 'synopsis', 'genre', 'author', 'year', 'created_at', 'updated_at')
