from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from comments.models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

