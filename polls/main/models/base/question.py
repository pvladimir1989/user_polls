from django.db import models

from main.models.base.poll import Poll

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
    possible_answers = models.JSONField(verbose_name="Возможные ответы", default=dict)

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

    def __str__(self):
        return self.text

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        print(1, self)
        if self is not None and self.poll is not None:
            print(2, self.poll, self.poll.start_date)
        if self is None or self.poll is None or self.poll.start_date is None:
            return super().save(force_insert, force_update, using, update_fields)
        print('false')
        return False