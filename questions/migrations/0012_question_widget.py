# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0011_quiz_question_widget'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='widget',
            field=models.CharField(default=b'1', help_text='How should the answers to this question be presented?', max_length=1, verbose_name='Widget', choices=[(b'1', 'Default'), (b'2', 'Radio Widget'), (b'3', 'Checkbox Widget')]),
        ),
    ]
