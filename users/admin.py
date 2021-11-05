from django.contrib import admin

from users.models import UserQuestion


class UserQuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question', 'created_at', 'ticket')
    list_display_links = ('id', 'ticket')
    search_fields = ('ticket', 'created_at')
    list_filter = ('ticket', 'created_at')


admin.site.register(UserQuestion)
