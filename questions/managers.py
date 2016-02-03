from django.db import models


class QuizManager(models.Manager):

    def active(self):
        return self.get_queryset().filter(draft=False)
