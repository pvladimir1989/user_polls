from rest_framework.serializers import ModelSerializer

from main.models import Poll


class PollSerializer(ModelSerializer):
    class Meta:
        model = Poll
        fields = "__all__"
