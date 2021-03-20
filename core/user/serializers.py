from rest_framework import serializers
from high.user.models import User
from abstract.serializers import AbstractSerializer


class UserSerializer(AbstractSerializer):

    class Meta:
        model = User
        fields = ['public_id', 'username', 'email', 'is_active', 'created', 'updated']
        read_only_field = ['is_active']
