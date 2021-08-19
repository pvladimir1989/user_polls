from django.views.generic import ListView

from main.models import Poll


class SelectedPollListView(ListView):
    model = Poll
    template_name = "main/selected_poll_with_questions.html"
