# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_review_sitting'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='public',
            field=models.BooleanField(default=False, help_text='Is this review open to all users?', verbose_name='Open'),
        ),
    ]
