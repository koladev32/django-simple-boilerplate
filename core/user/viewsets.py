from rest_framework import viewsets
from core.user.serializers import UserSerializer
from core.user.models import User

from rest_framework.permissions import IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]
        print(lookup_field_value)

        obj = User.objects.get_object_by_public_id(lookup_field_value)
        print(obj)
        self.check_object_permissions(self.request, obj)

        return obj

