from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from questions.models import Quiz


class PeerReview(models.Model):
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.PROTECT)
    quiz = models.ForeignKey(Quiz, verbose_name=_("Question Set"), on_delete=models.PROTECT)
    reviewers = models.ManyToManyField(User, verbose_name=_("Reviewers"), related_name='peer_reviewers')

    class Meta:
        verbose_name = _("Peer Review")
        verbose_name_plural = _("Peer Reviews")

    def __str__(self):
        return "{user} {quiz}".format(user=self.user.userprofile.get_display_name(), quiz=self.quiz.title)

    @models.permalink
    def get_absolute_url(self):
        return reverse('reviews:peer_review', args=[self.pk])
