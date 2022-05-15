from django.urls import path

from users.api.viewsets import UserViewSet

#

urlpatterns = [
    # path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    # path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserViewSet.as_view({'post': 'create'}), name='auth_register'),
]
