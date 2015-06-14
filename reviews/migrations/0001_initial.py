# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('title', models.CharField(max_length=300, verbose_name='Title', blank=True)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Question Set', to='questions.Quiz')),
                ('reviewers', models.ManyToManyField(related_name='peer_reviewers', verbose_name='Reviewers', to=settings.AUTH_USER_MODEL, blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='User')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
