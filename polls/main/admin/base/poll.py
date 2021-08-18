from django.contrib import admin

from main.models.base import Poll


# @admin.register(BaseUser)
class PollAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_date', 'end_date', 'description')
    search_fields = ('title',)


admin.site.register(Poll, PollAdmin)
