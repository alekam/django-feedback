from django.conf.urls.defaults import *

from feedback.views import leave_feedback
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', leave_feedback, name='leave-feedback'),
    url(r'^sended/$', direct_to_template, 
        {'template': 'feedback/sended.html'},
        name='feedback_sended'),
)
