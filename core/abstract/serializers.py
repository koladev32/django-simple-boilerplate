from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    
    id = serializers.UUIDField(read_only=True, format='hex', source='public_id')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
