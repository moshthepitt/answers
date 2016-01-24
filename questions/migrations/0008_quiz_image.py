# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import core.utils


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0007_auto_20151209_1526'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='image',
            field=models.ImageField(default=None, upload_to=core.utils.PathAndRename(b'quiz/'), null=True, verbose_name='Image', blank=True),
        ),
    ]
