from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.api.viewsets import UserViewSet, JwtTokenViewSet

#

urlpatterns = [
    path('login/', JwtTokenViewSet.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserViewSet.as_view({'post': 'create'}), name='auth_register'),
]
