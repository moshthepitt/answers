# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_auto_20150612_1703'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Question Set', 'verbose_name_plural': 'Question Sets'},
        ),
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, unique=True, populate_from=b'title'),
        ),
    ]
