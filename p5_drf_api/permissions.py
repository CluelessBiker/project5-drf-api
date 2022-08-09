from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Provide CRUD to user owned models.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
