# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20150516_1639'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['title'], 'verbose_name': 'Question', 'verbose_name_plural': 'Questions'},
        ),
        migrations.AlterField(
            model_name='multiplechoiceanswer',
            name='title',
            field=models.CharField(help_text='Input the answer as you want it displayed', max_length=300, verbose_name='Answer'),
        ),
    ]
