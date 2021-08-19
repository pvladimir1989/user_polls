from django.urls import path
from django.contrib import admin

from main.views.base.index import index
from main.views.base.selected_poll import selected_poll
from main.views.base.selected_question import SelectedQuestionDetailView

urlpatterns = [

    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('selected_questions/<int:pk>/', SelectedQuestionDetailView.as_view(), name='selected_questions'),
    path('selected_polls/<int:pk>/', selected_poll, name='selected_polls')

]
