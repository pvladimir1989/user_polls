from django.contrib import admin

from main.models.base import Answer


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('client_id', 'question', 'answer')
    search_fields = ('question',)


admin.site.register(Answer, AnswerAdmin)
