from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import ListModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from core.api.serializers import BookSerializer
from core.models import Book
from core.permissions import UserVerified


class CustomPaginator(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'


class BookViewSet(ListModelMixin, GenericViewSet):
    queryset = Book.objects.all().filter(restricted=False)
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = CustomPaginator
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['year', 'author', 'genre']
    search_fields = ['title', 'synopsis']


class RestrictedBookViewSet(ListModelMixin, GenericViewSet):
    queryset = Book.objects.all().filter(restricted=True)
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, UserVerified]
    pagination_class = CustomPaginator
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['year', 'author', 'genre']
    search_fields = ['title', 'synopsis']
