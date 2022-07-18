from rest_framework.serializers import ModelSerializer

from comments.models import Comment
from users.api.serializers import UserSerializer


class CommentSerializer(ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'comments', 'date', 'approved', 'book']
