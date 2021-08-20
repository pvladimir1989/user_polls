from rest_framework import serializers

from main.models import Poll


class ClientPoll(serializers.Serializer):
    client_id = serializers.IntegerField(required=True)
