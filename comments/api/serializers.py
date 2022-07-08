from rest_framework.serializers import ModelSerializer

from comments.models import Comment


class CommentSerializer(ModelSerializer):
    # user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'comments', 'date', 'approved', 'book']
