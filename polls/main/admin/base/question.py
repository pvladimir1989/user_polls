from django.contrib import admin

from main.models.base.poll import Poll
from main.models.base import Question


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'type_of_answer', 'poll', 'possible_answers')
    search_fields = ('poll',)
    formfield_overrides = {}

    def render_change_form(self, request, context, *args, **kwargs):
        print(context['adminform'].form.fields)
        if 'poll' in context['adminform'].form.fields:
            context['adminform'].form.fields['poll'].queryset = Poll.objects.filter(start_date=None)
        return super().render_change_form(request, context, *args, **kwargs)

    def has_change_permission(self, request, obj: Question = None):
        print(1, obj)
        if obj is not None and obj.poll is not None:
            print(2, obj.poll, obj.poll.start_date)
        if obj is None or obj.poll is None or obj.poll.start_date is None:
            return super(QuestionAdmin, self).has_change_permission(request)
        print('false')
        return True

    def has_delete_permission(self, request, obj=None):
        return self.has_change_permission(request, obj)


admin.site.register(Question, QuestionAdmin)
