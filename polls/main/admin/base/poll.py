from django.contrib import admin

from main.models.base import Poll


class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'end_date', 'description', 'start_date',)
    search_fields = ('title',)


admin.site.register(Poll, PollAdmin)
