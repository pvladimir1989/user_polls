from django.db import models

from main.models.base.poll import Poll


class Question(models.Model):
    text = models.TextField(null=True, blank=True, verbose_name="Текст вопроса")
    # type_of_question - надо подумать
    type_of_question = models.CharField(max_length=100)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name="Опрос")

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
