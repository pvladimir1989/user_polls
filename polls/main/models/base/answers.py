from django.db import models

from main.models.base.question import Question


class Answer(models.Model):
    client_id = models.IntegerField(verbose_name="Идентификатор клиента")
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Вопрос")
    answer = models.JSONField(verbose_name="Ответ", default=dict)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
