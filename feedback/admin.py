from django.contrib import admin
from feedback.models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message', 'time']
    search_fields = ['email', 'message']
    list_filter = ['time', ]
    date_hierarchy = 'time'
    raw_id_fields = ('user', )


admin.site.register(Feedback, FeedbackAdmin)
