from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsOwnerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        if request.method in ("POST", "PUT", "DELETE"):
            return request.user.is_authenticated and request.user.role == 'autor'

        return request.user.is_authenticated and request.user
