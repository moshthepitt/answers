from django.core.validators import MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.utils.encoding import python_2_unicode_compatible

from autoslug import AutoSlugField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from polymorphic.models import PolymorphicModel
from sorl.thumbnail import ImageField

from core.utils import PathAndRename
from saas.models import Customer
from .managers import QuizManager


@python_2_unicode_compatible
class Category(MPTTModel):

    """Category Model"""

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    title = models.CharField(_("Category Title"), max_length=300, blank=False, help_text=_(
        "The category title as you want it displayed"))
    description = models.TextField(
        _("Description"), blank=True, help_text=_("A more detailed description of the category"))
    parent = TreeForeignKey("Category", blank=True, null=True, default=None,
                            verbose_name=_("Parent Category"), on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, verbose_name=_(
        "Customer"), on_delete=models.PROTECT, blank=True, null=True, default=None)
    active = models.BooleanField(_("Active"), default=True)
    # Sortable property
    order = models.PositiveIntegerField()

    class MPTTMeta:
        order_insertion_by = ['order']

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")
        ordering = ['order']

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Sitting(models.Model):

    """
    A sitting is a relationship between a Review and a Quiz
    for example if you want to use a certain Quiz as a peer review,
    it would make sense to have a session to relate them
    so that you can get the peer review's average score using the session
    instead of the quiz (because a Quiz is reusable)
    """
    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    title = models.CharField(_("Title"), max_length=300, blank=False)
    customer = models.ForeignKey(Customer, verbose_name=_(
        "Customer"), on_delete=models.PROTECT, blank=True, null=True, default=None)
    start = models.DateTimeField(_("Start"), blank=True, null=True, default=None, help_text=_(
        "The time at which the user starts answering the questions"))
    end = models.DateTimeField(_("End"), blank=True, null=True, default=None, help_text=_(
        "The time at which the uer stops answering the questions"))
    duration = models.PositiveIntegerField(_("Duration"), blank=True, null=True, default=None, help_text=_(
        "The time allowed (in minutes) for the user to answer then questions"))
    strict_duration = models.BooleanField(_("Strict Duration"), default=False, help_text=_(
        "If True, no answers will be saved to the database after the duration is exceeded"))

    class Meta:
        verbose_name = _("Sitting")
        verbose_name_plural = _("Sittings")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Quiz(models.Model):

    """A quiz is a collection of questions"""

    # ordering choices
    DATE_ORDER = '1'
    ALPHABETICAL_ORDER = '2'
    RANDOM_ORDER = '3'
    ORDER_FIELD = '4'

    QUESTION_ORDERING_CHOICES = (
        (DATE_ORDER, _('Date')),
        (ALPHABETICAL_ORDER, _('Alphabetical')),
        (RANDOM_ORDER, _('Random')),
        (ORDER_FIELD, _('Use Question Order Field')),
    )

    # question widget type choices
    DEFAULT_WIDGET = '1'
    RADIO_WIDGET = '2'
    CHECKBOX_WIDGET = '3'

    QUESTION_WIDGET_CHOICES = (
        (DEFAULT_WIDGET, _('Default')),
        (RADIO_WIDGET, _('Radio Widget')),
        (CHECKBOX_WIDGET, _('Checkbox Widget')),
    )

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    title = models.CharField(_("Title"), max_length=300, blank=False)
    slug = AutoSlugField(
        populate_from='title', editable=True, unique=True, null=False, max_length=255)
    image = ImageField(_("Image"), upload_to=PathAndRename(
        "quiz/"), blank=True, null=True, default=None)
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name=_("Category"), on_delete=models.PROTECT)
    customer = models.ForeignKey(Customer, verbose_name=_(
        "Customer"), on_delete=models.PROTECT, blank=True, null=True, default=None)
    description = models.TextField(
        _("Description"), blank=True, help_text=_("A more detailed description of the question set"))
    question_ordering = models.CharField(
        _("Question Ordering"), max_length=1, choices=QUESTION_ORDERING_CHOICES, blank=False, default=ALPHABETICAL_ORDER, help_text=_("How should the questions in this question set be ordered?"))
    question_widget = models.CharField(
        _("Question Widget"), max_length=1, choices=QUESTION_WIDGET_CHOICES, blank=False, default=DEFAULT_WIDGET, help_text=_("How should the answers to questions in this question set be presented?"))
    max_questions = models.PositiveIntegerField(
        blank=True, null=True, default=None, verbose_name=_("Max Questions"),
        help_text=_("Number of questions to be answered on each attempt."))
    answers_after_question = models.BooleanField(
        blank=False, default=False,
        help_text=_("Show answers after each question?"),
        verbose_name=_("Answers after question"))
    answers_at_end = models.BooleanField(
        blank=False, default=False,
        help_text=_("Show answers at the end of the whole quiz?"),
        verbose_name=_("Answers at end"))
    single_attempt = models.BooleanField(
        blank=False, default=True,
        help_text=_("If yes, only one attempt by"
                    " a user will be permitted."
                    " Non users cannot sit this exam."),
        verbose_name=_("Single Attempt"))
    pass_mark = models.SmallIntegerField(
        blank=True, default=0,
        help_text=_("Percentage required to pass exam."),
        validators=[MaxValueValidator(100)])
    success_text = models.TextField(
        blank=True, help_text=_("Displayed if user passes."),
        verbose_name=_("Success Text"))
    fail_text = models.TextField(
        verbose_name=_("Fail Text"),
        blank=True, help_text=_("Displayed if user fails."))
    draft = models.BooleanField(
        blank=False, default=False,
        verbose_name=_("Draft"),
        help_text=_("If yes, the quiz is not displayed"
                    " in the quiz list and can only be"
                    " taken by users who can edit"
                    " quizzes."))

    objects = QuizManager()

    def get_question_order(self):
        if self.question_ordering == Quiz.DATE_ORDER:
            return "created_on"
        elif self.question_ordering == Quiz.ALPHABETICAL_ORDER:
            return "title"
        elif self.question_ordering == Quiz.RANDOM_ORDER:
            return "?"
        elif self.question_ordering == Quiz.ORDER_FIELD:
            return "order"
        else:
            return "title"

    def get_questions(self):
        return self.question_set.all().order_by(self.get_question_order())

    def get_absolute_url(self):
        return reverse('questions:quiz', args=[self.slug])

    class Meta:
        verbose_name = _("Question Set")
        verbose_name_plural = _("Question Sets")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Question(PolymorphicModel):

    """
    Base class for all types of questions
    """

    # question widget type choices
    DEFAULT_WIDGET = '1'
    RADIO_WIDGET = '2'
    CHECKBOX_WIDGET = '3'

    WIDGET_CHOICES = (
        (DEFAULT_WIDGET, _('Default')),
        (RADIO_WIDGET, _('Radio Widget')),
        (CHECKBOX_WIDGET, _('Checkbox Widget')),
    )

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    quiz = models.ForeignKey(Quiz, verbose_name=_("Quuestion Set"), on_delete=models.PROTECT)
    title = models.CharField(
        _("Question"), max_length=300, blank=False, help_text=_("The question as you want it displayed"))
    description = models.TextField(
        _("Description"), blank=True, help_text=_("A more detailed description of the question"))
    image = ImageField(_("Image"), upload_to=PathAndRename(
        "questions/"), blank=True, null=True, default=None)
    required = models.BooleanField(
        _("Required"), default=True, help_text=_("Is this question required?"))
    explanation = models.TextField(_("Explanation"), blank=True, help_text=_(
        "Explanation to be shown after the question has been answered"))
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name=_("Category"), on_delete=models.PROTECT)
    widget = models.CharField(
        _("Widget"), max_length=1, choices=WIDGET_CHOICES, blank=False, default=DEFAULT_WIDGET, help_text=_("How should the answers to this question be presented?"))
    # Sortable property
    order = models.PositiveIntegerField()

    def _has_image_answers(self):
        if isinstance(self, MultipleChoiceQuestion):
            return MultipleChoiceOption.objects.filter(question=self).exclude(image=None).exists()
        return False

    @property
    def has_image_answers(self):
        return self._has_image_answers()

    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ['title']

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class TextQuestion(Question):

    """A type of question that expects short text answers"""

    class Meta:
        verbose_name = _("Text Question")
        verbose_name_plural = _("Text Questions")

    def get_answer_class(self):
        from answers.models import TextAnswer
        return TextAnswer

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class EssayQuestion(Question):

    """A type of question that expects essay type answers"""

    class Meta:
        verbose_name = _("Essay Question")
        verbose_name_plural = _("Essay Questions")

    def get_answer_class(self):
        from answers.models import EssayAnswer
        return EssayAnswer

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class MultipleChoiceQuestion(Question):

    """
        A type of question where the user is presented with a list of options to pick from
        The choices themselves are MultipleChoiceAnswer objects
    """

    class Meta:
        verbose_name = _("Multiple Choice Question")
        verbose_name_plural = _("Multiple Choice Questions")

    def get_answer_class(self):
        from answers.models import MultipleChoiceAnswer
        return MultipleChoiceAnswer

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class MultipleChoiceOption(models.Model):

    """The answer choices to a multipel choice question"""

    created_on = models.DateTimeField(_("Created on"), auto_now_add=True)
    updated_on = models.DateTimeField(_("Updated on"), auto_now=True)
    question = models.ForeignKey(MultipleChoiceQuestion, verbose_name=_("Question"), on_delete=models.CASCADE)
    title = models.CharField(_("Answer"), max_length=300, blank=False, help_text=_(
        "Input the answer as you want it displayed"))
    image = ImageField(_("Image"), upload_to=PathAndRename(
        "multiple-choice-options/"), blank=True, null=True, default=None)
    correct_answer = models.BooleanField(
        _("Correct Answer"), default=False, help_text=_("Is this a correct answer?"))
    other = models.BooleanField(_("Other Option"), default=False, help_text=_(
        "This field will present an option to input text instead of one of the presented choices"))

    class Meta:
        verbose_name = _("Multiple Choice Answer")
        verbose_name_plural = _("Multiple Choice Answers")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class RatingQuestion(Question):

    """A question used to rate things from Very Poor/Very Bad to Very Good"""

    class Meta:
        verbose_name = _("Rating Question")
        verbose_name_plural = _("Rating Questions")

    def get_answer_class(self):
        from answers.models import RatingAnswer
        return RatingAnswer

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class BooleanQuestion(Question):

    """A type of question where the user is expected to select from two options: True/False, Yes/No, etc"""

    true_label = models.CharField(_("True Label"), max_length=50, default=_(
        "True"), help_text=_("What will represent the True/Yes option"))
    false_label = models.CharField(_("False Label"), max_length=50, default=_(
        "False"), help_text=_("What will represent the False/No option"))
    correct_answer = models.NullBooleanField(_("Correct Answer"), blank=True, null=True, default=None, help_text=_(
        "Which is the correct answer to this question?"))

    class Meta:
        verbose_name = _("Boolean Question")
        verbose_name_plural = _("Boolean Questions")

    def get_answer_class(self):
        from answers.models import BooleanAnswer
        return BooleanAnswer

    def __str__(self):
        return self.title
