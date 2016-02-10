# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0014_auto_20160210_0406'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='multiplechoiceoption',
            options={'ordering': ['created_on'], 'verbose_name': 'Multiple Choice Answer', 'verbose_name_plural': 'Multiple Choice Answers'},
        ),
        migrations.AddField(
            model_name='quiz',
            name='show_question_numbers',
            field=models.BooleanField(default=False, help_text='Use the question.order field as question numbers', verbose_name='Show question numbers'),
        ),
    ]
