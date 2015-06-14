from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from questions.models import Quiz


class Review(models.Model):
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    title = models.CharField(_("Title"), max_length=300, blank=True)
    user = models.ForeignKey(User, verbose_name=_("User"), on_delete=models.PROTECT, blank=True, null=True, default=None)
    quiz = models.ForeignKey(Quiz, verbose_name=_("Question Set"), on_delete=models.PROTECT)
    reviewers = models.ManyToManyField(User, verbose_name=_("Reviewers"), related_name='peer_reviewers', blank=True)

    class Meta:
        verbose_name = _("Review")
        verbose_name_plural = _("Reviews")

    def __str__(self):
        if self.title:
            return self.title
        elif self.user:
            return "{user} {quiz}".format(user=self.user.userprofile.get_display_name(), quiz=self.quiz.title)
        else:
            return "{quiz}".format(quiz=self.quiz.title)

    def get_absolute_url(self):
        return reverse('reviews:review', args=[self.pk])
