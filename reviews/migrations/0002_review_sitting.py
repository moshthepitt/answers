# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_sitting'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='sitting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='questions.Sitting', null=True, verbose_name='Sitting'),
        ),
    ]
