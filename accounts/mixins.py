from rest_framework import permissions
from .permissions import IsAdmin, IsNormalUsers, IsStaffUsers
from rest_framework.authentication import TokenAuthentication

class IsAdminMixin:
    permission_classes = [permissions.IsAuthenticated, IsAdmin]
    authentication_classes = [TokenAuthentication]

class IsNormalUsersMixin:
    permission_classes = [permissions.IsAuthenticated, IsNormalUsers]
    authentication_classes = [TokenAuthentication]

class IsStaffUsersMixin:
    permission_classes = [permissions.IsAuthenticated, IsStaffUsers]
    authentication_classes = [TokenAuthentication]