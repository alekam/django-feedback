from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.contrib import messages

from feedback.forms import FeedbackForm

def leave_feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        if request.user.is_authenticated():
            feedback.user = request.user
            messages.add_message(request, messages.INFO, _("Your feedback has been saved successfully."))
        feedback.save()
        return HttpResponseRedirect(request.GET.get('next', request.META.get('HTTP_REFERER', '/')))
    return render_to_response('feedback/feedback_form.html', {'form': form}, context_instance=RequestContext(request))
