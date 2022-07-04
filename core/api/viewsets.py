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
    filterset_fields = ['year', 'author', 'genre']
    search_fields = ['title', 'synopsis']


class RestrictedBookViewSet(ListModelMixin, GenericViewSet):
    queryset = Book.objects.all().filter(restricted=True)
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated, UserVerified]
    pagination_class = CustomPaginator
    filterset_fields = ['year', 'author', 'genre']
    search_fields = ['title', 'synopsis']


"""
    def get_query(self):
        id = self.request.query_params.get('id', None)
        author = self.request.query_params.get('author', None)
        genre = self.request.query_params.get('genre', None)
        title = self.request.query_params.get('title', None)
        synopsis = self.request.query_params.get('synpsis', None)
        
        if id:
            queryset = Books.objects.filter(pk=id)
            
        if author:
            queryset = queryset.filter(author__iexact=author)
            
        if genre:
            queryset = queryset.filter(genre__iexact=genre)
            
        if title:
            queryset = queryset.filter(title__iexact=title)
            
        if synopsis:
            queryset = queryset.filter(synopsis__iexact=synopsis)
            
        return queryset
"""
