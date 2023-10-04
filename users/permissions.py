# from myapp.models import *
from rest_framework.permissions import BasePermission


# User = get_user_model()


class IsAdminUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_admin)
