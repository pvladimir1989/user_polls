from unittest import result

from rest_framework.viewsets import ViewSet
from main.models import Poll, Answer, Question

from main.serializers.base.client_poll import ClientPoll as Client_poll_ser

from rest_framework.response import Response

from django.db.models.expressions import Q, Subquery


# APIView
class ClientPoll(ViewSet):
    def list(self, request):
        serializer = Client_poll_ser(data=request.query_params)
        result = []
        if serializer.is_valid():
            client_id = serializer.data.get('client_id', 0)
            q = Poll.objects.filter(question__answer__client_id=client_id)

            x: Poll
            for x in q:
                answers = []
                for y in x.question_set.all():
                    answers.append(
                        {
                            'url': '#1123',
                            'quest': str(y),
                            'answ': str(y.answer_set.all().first())
                        }
                    )
                result.append(
                    {
                        "poll": str(x),
                        'url': '#1123',
                        'answs':answers
                    }
                )

        return Response({"result": result})

