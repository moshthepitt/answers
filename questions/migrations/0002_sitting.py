# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sitting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('title', models.CharField(max_length=300, verbose_name='Title', blank=True)),
            ],
            options={
                'verbose_name': 'Sitting',
                'verbose_name_plural': 'Sittings',
            },
        ),
    ]
