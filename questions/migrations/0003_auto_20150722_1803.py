# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_sitting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='single_attempt',
            field=models.BooleanField(default=True, help_text='If yes, only one attempt by a user will be permitted. Non users cannot sit this exam.', verbose_name='Single Attempt'),
        ),
    ]
