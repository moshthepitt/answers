# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields
import core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0008_quiz_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoiceoption',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=None, upload_to=core.utils.PathAndRename(b'multiple-choice-options/'), null=True, verbose_name='Image', blank=True),
        ),
        migrations.AddField(
            model_name='sitting',
            name='duration',
            field=models.PositiveIntegerField(default=None, help_text='The time allowed (in minutes) for the user to answer then questions', null=True, verbose_name='Duration', blank=True),
        ),
        migrations.AddField(
            model_name='sitting',
            name='end',
            field=models.DateTimeField(default=None, help_text='The time at which the uer stops answering the questions', null=True, verbose_name='End', blank=True),
        ),
        migrations.AddField(
            model_name='sitting',
            name='start',
            field=models.DateTimeField(default=None, help_text='The time at which the user starts answering the questions', null=True, verbose_name='Start', blank=True),
        ),
        migrations.AddField(
            model_name='sitting',
            name='strict_duration',
            field=models.BooleanField(default=False, help_text='If True, no answers will be saved to the database after the duration is exceeded', verbose_name='Strict Duration'),
        ),
        migrations.AlterField(
            model_name='question',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=None, upload_to=core.utils.PathAndRename(b'questions/'), null=True, verbose_name='Image', blank=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='image',
            field=sorl.thumbnail.fields.ImageField(default=None, upload_to=core.utils.PathAndRename(b'quiz/'), null=True, verbose_name='Image', blank=True),
        ),
    ]
