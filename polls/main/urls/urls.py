from django.urls import path

from main.views import index
from django.contrib import admin

from main.views.base.selected_poll import SelectedPollListView
from main.views.base.selected_question import SelectedQuestionDetailView

urlpatterns = [

    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('selected_questions/<int:pk>/', SelectedQuestionDetailView.as_view(), name='selected_questions'),
    path('selected_polls/', SelectedPollListView.as_view(), name='selected_polls')

]
