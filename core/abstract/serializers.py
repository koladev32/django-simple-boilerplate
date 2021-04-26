from rest_framework import serializers


class AbstractSerializer(serializers.ModelSerializer):
    
    public_id = serializers.UUIDField(read_only=True, format='hex')
    created = serializers.DateTimeField(read_only=True)
    updated = serializers.DateTimeField(read_only=True)
