# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0005_auto_20160203_1247'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='no_login',
            field=models.BooleanField(default=False, help_text='Is this review open to the world?', verbose_name='No Login'),
        ),
    ]
