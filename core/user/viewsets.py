from rest_framework import viewsets
from user.serializers import AbstractSerializer
from user.models import User

from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    permission_classes = (IsAuthenticated, )
    serializer_class = (AbstractSerializer, )


