from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from core.api.serializers import BookSerializer
from core.models import Book


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
