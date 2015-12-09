# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0006_auto_20151209_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitting',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Title'),
        ),
    ]
