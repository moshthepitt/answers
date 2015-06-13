from django.db import models
from django.utils.translation import ugettext_lazy as _

from polymorphic import PolymorphicModel

from questions.models import Question, MultipleChoiceOption


class Answer(PolymorphicModel):
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    question = models.ForeignKey(Question, verbose_name=_("Question"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")

    def __str__(self):
        return self.question.title


class TextAnswer(Answer):
    answer = models.CharField(_("Answer"), max_length=255)

    class Meta:
        verbose_name = ("Text Answer")
        verbose_name_plural = ("Text Answers")

    def __str__(self):
        return self.question.title


class EssayAnswer(Answer):
    answer = models.TextField(_("Answer"))

    class Meta:
        verbose_name = _("Essay Answer")
        verbose_name_plural = _("Essay Answers")

    def __str__(self):
        return self.question.title


class MultipleChoiceAnswer(Answer):
    answer = models.ForeignKey(MultipleChoiceOption, verbose_name=_("Answer"), on_delete=models.PROTECT)

    class Meta:
        verbose_name = _("Multiple Choice Answer")
        verbose_name_plural = _("Multiple Choice Answers")

    def __str__(self):
        return self.question.title


class RatingAnswer(Answer):
    # choices
    VERY_POOR = 1
    POOR = 2
    AVERAGE = 3
    GOOD = 4
    VERY_GOOD = 5

    RATING_CHOICES = (
        (VERY_POOR, _('Very Poor')),
        (POOR, _('Poor')),
        (AVERAGE, _('Average')),
        (GOOD, _("Good")),
        (VERY_GOOD, _("Very Good")),
    )

    answer = models.PositiveIntegerField(_("Answer"), choices=RATING_CHOICES)

    class Meta:
        verbose_name = _("Rating Answer")
        verbose_name_plural = _("Rating Answers")

    def __str__(self):
        return self.question.title


class BooleanAnswer(Answer):
    answer = models.BooleanField(_("Answer"))

    class Meta:
        verbose_name = _("Boolean Answer")
        verbose_name_plural = _("Boolean Answers")

    def __str__(self):
        return self.question.title
