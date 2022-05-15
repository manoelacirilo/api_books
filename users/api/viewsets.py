from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView

from users.api.serializers import UserSerializer, JwtTokenSerializer
from users.models import User


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class JwtTokenViewSet(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = JwtTokenSerializer