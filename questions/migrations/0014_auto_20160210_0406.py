# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0013_auto_20160210_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='question',
            name='order',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
