from core.user.models import User
from core.abstract.serializers import AbstractSerializer


class UserSerializer(AbstractSerializer):

    class Meta:
        model = User
        fields = ['public_id', 'username', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active']
