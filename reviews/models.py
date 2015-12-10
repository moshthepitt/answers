from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

from questions.models import Quiz, Sitting
from users.models import UserProfile
from saas.models import Customer


@python_2_unicode_compatible
class Review(models.Model):
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    title = models.CharField(_("Title"), max_length=300, blank=True)
    customer = models.ForeignKey(Customer, verbose_name=_(
        "Customer"), on_delete=models.PROTECT, blank=True, null=True, default=None)
    userprofile = models.ForeignKey(UserProfile, verbose_name=_("User"), help_text=_(
        "The person being reviewed"), on_delete=models.PROTECT, blank=True, null=True, default=None)
    sitting = models.ForeignKey(
        Sitting, verbose_name=_("Sitting"), on_delete=models.PROTECT, blank=True, null=True, default=None)
    quiz = models.ForeignKey(Quiz, verbose_name=_("Question Set"), on_delete=models.PROTECT)
    reviewers = models.ManyToManyField(UserProfile, verbose_name=_("Reviewers"), help_text=_(
        "The people who are going to take this review"), related_name='peer_reviewers', blank=True)
    public = models.BooleanField(_("Open"), default=False, help_text=_("Is this review open to all users?"))

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")
        ordering = ['created_on']

    def __str__(self):
        if self.userprofile:
            if self.title:
                return _("{title}: {user}").format(title=self.title, user=self.userprofile.get_display_name())
            else:
                return _("{0}: {1}").format(self.quiz.title, self.userprofile.get_display_name())
        elif self.title:
            return self.title
        else:
            return "{quiz}".format(quiz=self.quiz.title)

    def get_absolute_url(self):
        return reverse('reviews:review', args=[self.pk])
