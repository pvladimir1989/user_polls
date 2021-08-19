from django.views.generic import DetailView

from main.models import Question


class SelectedQuestionDetailView(DetailView):
    model = Question
    template_name = "main/selected_question_and_its_answers.html"
