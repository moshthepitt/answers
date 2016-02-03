# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_review_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='duration',
            field=models.PositiveIntegerField(default=None, help_text='The time allowed (in minutes) for the user to answer then questions', null=True, verbose_name='Duration', blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='end',
            field=models.DateTimeField(default=None, help_text='The time at which the uer stops answering the questions', null=True, verbose_name='End', blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='start',
            field=models.DateTimeField(default=None, help_text='The time at which the user starts answering the questions', null=True, verbose_name='Start', blank=True),
        ),
        migrations.AddField(
            model_name='review',
            name='strict_duration',
            field=models.BooleanField(default=False, help_text='If True, no answers will be saved to the database after the duration is exceeded', verbose_name='Strict Duration'),
        ),
    ]
