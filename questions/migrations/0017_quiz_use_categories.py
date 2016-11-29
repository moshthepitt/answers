# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0016_auto_20161129_1607'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='use_categories',
            field=models.BooleanField(default=False, help_text='If yes, questions will be separated by categories.', verbose_name='Use Categories'),
        ),
    ]
