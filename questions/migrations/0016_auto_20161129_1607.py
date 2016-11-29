# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0015_auto_20160210_0550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='question_ordering',
            field=models.CharField(default=b'2', help_text='How should the questions in this question set be ordered?', max_length=1, verbose_name='Question Ordering', choices=[(b'1', 'Date'), (b'2', 'Alphabetical'), (b'3', 'Random'), (b'4', 'Use Question Order Field'), (b'5', 'Use Category')]),
        ),
    ]
