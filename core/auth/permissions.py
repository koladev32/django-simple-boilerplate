from rest_framework import permissions


class UserPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if view.basename in ['user']:
            return obj == request.user

        return False
