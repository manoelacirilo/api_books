from decouple import config
from rest_framework import status
from rest_framework.mixins import UpdateModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView

from users.api.serializers import UserSerializer, JwtTokenSerializer, UpdateUserSerializer, UserProfileSerializer
from users.models import User


class UserViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer


class JwtTokenViewSet(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = JwtTokenSerializer


class UserProfileViewSet(UpdateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        user = request.user
        serializer = UpdateUserSerializer(
            user,
            data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST)


class LogoutViewSet(GenericViewSet):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()

            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class TermsViewSet(GenericViewSet):
    permission_classes = (AllowAny,)

    def get(self, _):
        data = {'link': config('TERMS_LINK')}
        return Response(data)
