from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from users.api.viewsets import UserViewSet, JwtTokenViewSet, UserProfileViewSet, LogoutViewSet, TermsViewSet, \
    SendVerificationEmailViewSet, VerifyEmailViewSet

#

urlpatterns = [
    path('login/', JwtTokenViewSet.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserViewSet.as_view({'post': 'create'}), name='user_register'),
    path('profile/', UserProfileViewSet.as_view({'put': 'update', 'get': 'retrieve'}), name='profile'),
    path('logout/', LogoutViewSet.as_view({'post': 'post'}), name='user_logout'),
    path('terms/', TermsViewSet.as_view({'get': 'get'}), name='terms'),
    path('send_verification_email/', SendVerificationEmailViewSet.as_view({'post': 'send_email'}),
         name='send_verification_email'),
    path('verify_email/', VerifyEmailViewSet.as_view({'post': 'verify'})),
]
