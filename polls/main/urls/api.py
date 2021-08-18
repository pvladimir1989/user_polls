from django.urls import path, include
from rest_framework import routers

from main.views import PollViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register(r'poll', PollViewSet)
router.register(r'question', QuestionViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls
