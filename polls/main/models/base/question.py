from django.db import models

from main.models.base.poll import Poll

YES = 1
NO = 0
MARRIED_YES_NO_CHOICE = [(YES, "yes"), (NO, "no")]

TEXT = 0
RADIO = 1
CHECKBOX = 2

TYPE_OF_ANSWER_CHOICES = (
    (TEXT, 'текст'),
    (RADIO, 'один вариант'),
    (CHECKBOX, 'множество вариантов'),
)


class Question(models.Model):
    text = models.TextField(null=True, blank=True, verbose_name="Текст вопроса")
    type_of_answer = models.IntegerField(verbose_name="Тип вопроса", choices=TYPE_OF_ANSWER_CHOICES)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name="Опрос")
    answer = models.JSONField(verbose_name="Ответ", default=dict)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"
