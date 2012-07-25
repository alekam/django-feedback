from django.conf import settings
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _


__all__ = ['Feedback', ]


class Feedback(models.Model):
    user = models.ForeignKey(User, blank=True, null=True,
                             verbose_name=_('User'))
    name = models.CharField(_('Contact name'), max_length=75)
    email = models.EmailField(_('Email'))
    message = models.TextField(_('Message'))
    time = models.DateTimeField(_('Time'), auto_now_add=True)

    class Meta:
        ordering = ['-time']
        verbose_name = _('Feedback')
        verbose_name_plural = _('Feedbacks')

    def __unicode__(self):
        return self.message

    def get_absolute_url(self):
        return reverse('admin:view-feedback', args=[self.id])
