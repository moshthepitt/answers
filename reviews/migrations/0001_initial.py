# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
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
                ('reviewers', models.ManyToManyField(help_text='The people who are going to take this review', related_name='peer_reviewers', verbose_name='Reviewers', to='users.UserProfile', blank=True)),
                ('userprofile', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, to='users.UserProfile', blank=True, help_text='The person being reviewed', null=True, verbose_name='User')),
            ],
            options={
                'ordering': ['created_on'],
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
    ]
