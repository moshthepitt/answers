# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0004_multiplechoiceoption_other'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=True, unique=True, max_length=255, populate_from=b'title'),
        ),
    ]
