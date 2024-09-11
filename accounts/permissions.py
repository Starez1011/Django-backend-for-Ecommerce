from rest_framework.permissions import BasePermission
from .models import User

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user is None:
            return False
        user_type = User.objects.get(email=request.user)
        if user_type.is_admin:
            return True
        else:
            return False
        
class IsStaffUsers(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user is None:
            return False
        user_type = User.objects.get(email=request.user)
        if user_type.is_staffusers:
            return True
        else:
            return False

class IsNormalUsers(BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        if request.user is None:
            return False
        user_type = User.objects.get(email=request.user)
        if user_type.is_normalusers:
            return True
        else:
            return False
