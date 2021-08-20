from django.urls import path, include
from rest_framework import routers

from main.views import PollViewSet, QuestionViewSet, AnswerViewSet, ClientPoll

router = routers.DefaultRouter()
router.register(r'poll', PollViewSet)  # list of poll
router.register(r'question', QuestionViewSet)  # list question of poll poll_id -> list
router.register(r'answers', AnswerViewSet)
router.register(r'client_poll', ClientPoll, basename='client_poll')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
