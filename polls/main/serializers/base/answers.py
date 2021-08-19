from rest_framework.serializers import ModelSerializer

from main.models import Answer


class AnswerSerializer(ModelSerializer):
    class Meta:
        model = Answer
        fields = "__all__"