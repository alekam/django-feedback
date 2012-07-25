from django.conf import settings
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from feedback.forms import FeedbackForm
from annoying.decorators import JsonResponse


def leave_feedback(request):
    form = FeedbackForm(request.POST or None)
    if form.is_valid():
        feedback = form.save(commit=False)
        if request.user.is_authenticated():
            feedback.user = request.user
        feedback.save()

        print request.is_ajax()
        if request.is_ajax():
            return JsonResponse({'status': True})
        elif not getattr(settings, 'FEEDBACK_ON_SINGLE_PAGE', False):
            from django.contrib import messages
            messages.add_message(request, messages.INFO,
                    _("Your feedback has been saved successfully."))
            next_ = request.GET.get('next', request.META.get('HTTP_REFERER', '/'))
        else:
            next_ = reverse('feedback_sended')
        return HttpResponseRedirect(next_)

    if request.is_ajax():
        return JsonResponse({'status': False, 'errors': form.errors})
    return render_to_response('feedback/feedback_form.html', {'form': form},
                              context_instance=RequestContext(request))
