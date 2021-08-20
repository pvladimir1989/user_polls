import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet
from main.models import Poll

from main.serializers.base import PollSerializer
from rest_framework.permissions import IsAuthenticated

from django.db.models.expressions import Q


class PollViewSet(ReadOnlyModelViewSet):
    queryset = Poll.objects \
        .filter(~Q(start_date=None)) \
        .filter(Q(end_date=None) | Q(end_date__gte=datetime.datetime.now())) \
        .all()
    serializer_class = PollSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    permission_classes = [IsAuthenticated]
    filter_fields = ['end_date']




