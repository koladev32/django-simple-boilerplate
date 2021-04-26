from rest_framework import viewsets
from core.user.serializers import UserSerializer
from core.user.models import User

from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    permission_classes = (IsAuthenticated,)
    serializer_class = (UserSerializer,)

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()