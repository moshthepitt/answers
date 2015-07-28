# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0002_auto_20150622_2309'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceOtherAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('body', models.CharField(max_length=255, verbose_name='Text answer')),
                ('answer', models.ForeignKey(verbose_name='Answer', to='answers.MultipleChoiceAnswer')),
            ],
            options={
                'verbose_name': 'Multiple Choice Other Answer',
                'verbose_name_plural': 'Multiple Choice Other Answers',
            },
        ),
    ]
