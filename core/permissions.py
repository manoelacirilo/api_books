from django.http import Http404
from rest_framework.permissions import BasePermission


class UserVerified(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_verified:
            return True

        raise Http404
