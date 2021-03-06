from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ReadOnlyModelViewSet
from main.models import Question

from main.serializers.base import QuestionSerializer
from rest_framework.permissions import IsAuthenticated


class QuestionViewSet(ReadOnlyModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filter_fields = ['poll']
    search_fields = ['text']
