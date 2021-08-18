from django.contrib import admin

from main.models.base import Question


# @admin.register(BaseUser)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'type_of_answer', 'poll', 'possible_answers')
    search_fields = ('poll',)


admin.site.register(Question, QuestionAdmin)
