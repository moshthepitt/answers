# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0010_auto_20160203_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='question_widget',
            field=models.CharField(default=b'1', help_text='How should the answers to questions in this question set be presented?', max_length=1, verbose_name='Question Widget', choices=[(b'1', 'Default'), (b'2', 'Radio Widget'), (b'3', 'Checkbox Widget')]),
        ),
    ]
