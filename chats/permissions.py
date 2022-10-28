from math import perm
from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow owners of an object to edit it.
    Owners and admin users may delete it. 
    Assumes the model instance has an `user` attribute.
    """


    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'delete': 
            return obj.user == request.user or request.user.is_staff
        # Instance must have an attribute named `user`.
        return obj.user == request.user

    class IsAdminOrReadOnly(permissions.BasePermission):
        def has_object_permission(self, request, view, obj):
            if request.method in permissions.SAFE_METHODS:
                return True

            return request 