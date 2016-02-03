from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import python_2_unicode_compatible

from polymorphic.models import PolymorphicModel

from questions.models import Question, MultipleChoiceOption
from reviews.models import Review
from users.models import UserProfile


@python_2_unicode_compatible
class Answer(PolymorphicModel):
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    question = models.ForeignKey(Question, verbose_name=_("Question"), on_delete=models.PROTECT)
    userprofile = models.ForeignKey(
        UserProfile, verbose_name=_("User"), on_delete=models.PROTECT, blank=True, null=True, default=None)
    review = models.ForeignKey(Review, verbose_name=_(
        "Review"), on_delete=models.PROTECT, blank=True, null=True, default=None)

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")

    def __str__(self):
        return self.question.title


@python_2_unicode_compatible
class TextAnswer(Answer):
    answer = models.CharField(_("Answer"), max_length=255)

    class Meta:
        verbose_name = ("Text Answer")
        verbose_name_plural = ("Text Answers")

    def __str__(self):
        return self.question.title


@python_2_unicode_compatible
class EssayAnswer(Answer):
    answer = models.TextField(_("Answer"))

    class Meta:
        verbose_name = _("Essay Answer")
        verbose_name_plural = _("Essay Answers")

    def __str__(self):
        return self.question.title


@python_2_unicode_compatible
class MultipleChoiceAnswer(Answer):
    answer = models.ForeignKey(
        MultipleChoiceOption, verbose_name=_("Answer"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Multiple Choice Answer")
        verbose_name_plural = _("Multiple Choice Answers")

    def __str__(self):
        return self.question.title


@python_2_unicode_compatible
class MultipleChoiceOtherAnswer(models.Model):
    """
    The text input when the "Other" option of a multiple choice questions is selected
    """
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    answer = models.ForeignKey(MultipleChoiceAnswer, verbose_name=_("Answer"), on_delete=models.CASCADE)
    body = models.CharField(_("Text answer"), max_length=255)

    class Meta:
        verbose_name = _("Multiple Choice Other Answer")
        verbose_name_plural = _("Multiple Choice Other Answers")

    def __str__(self):
        return self.body


@python_2_unicode_compatible
class RatingAnswer(Answer):
    # choices
    VERY_POOR = 1
    POOR = 2
    AVERAGE = 3
    GOOD = 4
    VERY_GOOD = 5

    RATING_CHOICES = (
        (VERY_POOR, _('Strongly Disagree')),
        (POOR, _('Disagree')),
        (AVERAGE, _('Neither Agree Nor Disagree')),
        (GOOD, _("Agree")),
        (VERY_GOOD, _("Strongly Agree")),
    )

    answer = models.PositiveIntegerField(_("Answer"), choices=RATING_CHOICES)

    class Meta:
        verbose_name = _("Rating Answer")
        verbose_name_plural = _("Rating Answers")

    def __str__(self):
        return self.question.title


@python_2_unicode_compatible
class BooleanAnswer(Answer):
    answer = models.BooleanField(_("Answer"))

    class Meta:
        verbose_name = _("Boolean Answer")
        verbose_name_plural = _("Boolean Answers")

    def __str__(self):
        return self.question.title
