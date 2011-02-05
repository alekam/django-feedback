from django.contrib import admin
from django.conf.urls.defaults import *
from django.template import RequestContext
from django.shortcuts import get_object_or_404, render_to_response

from feedback.models import Feedback

class FeedbackAdmin(admin.ModelAdmin):
    list_display = ['type', 'time', 'user', 'message', ]
    search_fields = ['user', 'message']
    list_filter = ['type', 'time']
    date_hierarchy = 'time'

admin.site.register(Feedback, FeedbackAdmin)
