# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('is_manager', models.BooleanField(default=False, help_text='Is this user a manager', verbose_name='Is Manager')),
                ('is_admin', models.BooleanField(default=False, help_text='Should this user have administrative privileges', verbose_name='Is Administrator')),
                ('manager', models.ForeignKey(default=None, to='users.UserProfile', blank=True, help_text="Select this user's manager", null=True, verbose_name='Manager')),
                ('user', models.OneToOneField(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['user__first_name', 'created_on'],
                'verbose_name': 'Staff Profile',
                'verbose_name_plural': 'Staff Profiles',
            },
        ),
    ]
