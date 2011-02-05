from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from feedback.forms import FeedbackForm
from django.core.urlresolvers import reverse

def leave_feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        if request.user.is_authenticated():
            feedback.user = request.user
            if not getattr(settings, 'FEEDBACK_ON_SINGLE_PAGE', False):
                from django.contrib import messages
                messages.add_message(request, messages.INFO, _("Your feedback has been saved successfully."))
                next = request.GET.get('next', request.META.get('HTTP_REFERER', '/'))
            else:
                next = reverse('feedback_sended')
        feedback.save()
        return HttpResponseRedirect(next)
    return render_to_response('feedback/feedback_form.html', {'form': form}, context_instance=RequestContext(request))
