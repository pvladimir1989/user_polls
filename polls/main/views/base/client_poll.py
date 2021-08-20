from rest_framework.viewsets import ViewSet
from main.models import Poll

from main.serializers.base.client_poll import ClientPoll as Client_poll_ser

from rest_framework.response import Response

from django.db.models.expressions import Q


# APIView
class ClientPoll(ViewSet):
    def list(self, request):
        polls = Poll.objects.all()
        serializer = Client_poll_ser(data=request.query_params)
        if serializer.is_valid():
            print('succeess')
        return Response({"polls": serializer.data})
