from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import Post


class IsAuthorOrReadOnly(BasePermission):
    """
    Custom permission to only allow authors of a post to edit or delete it.
    Read permissions are allowed to any request,
    so we'll always allow GET, HEAD or OPTIONS requests.
    """

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True
        else:
            return obj.author == request.user
