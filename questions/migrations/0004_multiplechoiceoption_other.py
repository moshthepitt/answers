# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20150722_1803'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplechoiceoption',
            name='other',
            field=models.BooleanField(default=False, help_text='This field will present an option to input text instead of one of the presented choices', verbose_name='Other Option'),
        ),
    ]
