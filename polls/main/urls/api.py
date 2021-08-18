from django.urls import path, include
from rest_framework import routers

from main.views import PollViewSet, QuestionViewSet

router = routers.DefaultRouter()
router.register(r'poll', PollViewSet) # list of poll
router.register(r'question', QuestionViewSet) # list question of poll poll_id -> list
# answers client_id --> list

'''
1 select active date end is none poll and select question
2 list of my answers filter by userclient_id
3 create new answer

answer - user
poll - user select from poll where subquery user in answer

'''

urlpatterns = [
    path('v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += router.urls
