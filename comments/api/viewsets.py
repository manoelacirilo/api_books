from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from comments.models import Comment
from .serializers import CommentSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def update(self, request, *args, **kwargs):
        comment = self.get_object()
        serializer = CommentSerializer(comment, data=request.data)

        if serializer.is_valid():
            if comment.user == request.user:
                serializer.save()
                return Response(serializer.data)

            return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        comment = self.get_object()

        if comment.user == request.user:
            self.perform_destroy(comment)
            return Response(status=status.HTTP_204_NO_CONTENT)

        return Response({"detail": "Not found."}, status.HTTP_404_NOT_FOUND)
