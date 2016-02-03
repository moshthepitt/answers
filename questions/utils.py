from django.forms import ModelChoiceField, RadioSelect
from django.utils import timezone

from .models import Sitting


def multiplechoice_to_radio(f, **kwargs):
    if isinstance(f.formfield(), ModelChoiceField):
        new_field = f.formfield()
        new_field.empty_label = None
        new_field.widget = RadioSelect()
        return new_field
    return f.formfield()


def generate_sitting(quiz, review):
    date_time = timezone.now()
    if quiz:
        title = "Quiz #{0} Review #{1} {2}".format(quiz.pk, review.pk, date_time.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        title = "Review #{0} {1}".format(review.pk, date_time.strftime("%Y-%m-%d %H:%M:%S"))
    sitting = Sitting(title=title)
    sitting.save()
    return sitting
