# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['user__first_name', 'created_on'], 'verbose_name': 'Staff Profile', 'verbose_name_plural': 'Staff Profiles'},
        ),
        migrations.AddField(
            model_name='userprofile',
            name='is_manager',
            field=models.BooleanField(default=False, help_text='Is this user a manager', verbose_name='Is Manager'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='manager',
            field=models.ForeignKey(default=None, to='users.UserProfile', blank=True, help_text="Select this user's manager", null=True, verbose_name='Manager'),
        ),
    ]
