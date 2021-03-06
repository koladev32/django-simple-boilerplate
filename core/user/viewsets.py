from core.user.serializers import UserSerializer
from core.user.models import User
from core.abstract.viewsets import AbstractViewSet


class UserViewSet(AbstractViewSet):
    http_method_names = ['get']
    serializer_class = UserSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            return User.objects.all()

    def get_object(self):
        lookup_field_value = self.kwargs[self.lookup_field]

        obj = User.objects.get_object_by_public_id(lookup_field_value)
        self.check_object_permissions(self.request, obj)

        return obj

