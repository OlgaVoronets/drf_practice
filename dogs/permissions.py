from rest_framework.permissions import BasePermission

from users.models import UserRoles


class IsModerator(BasePermission):
    """Проверка на модератора"""
    def has_permission(self, request, view):
        return request.user.role == UserRoles.MODERATOR


class IsDogPublic(BasePermission):
    "Проверка статуса собаки"
    def has_object_permission(self, request, view, obj):
        return obj.is_public


class IsDogOwner(BasePermission):
    "Проверка владельца собаки"

    def has_object_permission(self, request, view, obj):
        return request.user == obj.owner
