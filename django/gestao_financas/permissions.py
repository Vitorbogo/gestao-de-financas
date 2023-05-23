from rest_framework.permissions import BasePermission


class ReadUserRevenue(BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj) -> bool:
        """Check user is trying to edir their own revenue"""
        return obj.user_id == request.user.id