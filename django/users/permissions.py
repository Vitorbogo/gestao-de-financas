from rest_framework.permissions import BasePermission


class UpdateOwnProfile(BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj) -> bool:
        """Check user is trying to edir their own profile"""
        return obj == request.user
