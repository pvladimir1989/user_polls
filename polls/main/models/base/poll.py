from django.db import models


class Poll(models.Model):
    title = models.CharField(max_length=200, verbose_name="Название опроса")
    start_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    end_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата окончания")
    description = models.TextField(null=True, blank=True, verbose_name="Описание")

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

    def __str__(self):
        return self.title



