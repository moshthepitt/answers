# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=300, verbose_name='Group Name')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'User Group',
                'verbose_name_plural': 'User Groups',
            },
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'ordering': ['user__first_name', 'created_on'], 'verbose_name': 'User Profile', 'verbose_name_plural': 'User Profiles'},
        ),
        migrations.AddField(
            model_name='usergroup',
            name='manager',
            field=models.ForeignKey(default=None, blank=True, to='users.UserProfile', null=True, verbose_name='Group Manager'),
        ),
        migrations.AddField(
            model_name='usergroup',
            name='parent',
            field=models.ForeignKey(default=None, blank=True, to='users.UserGroup', null=True, verbose_name='Parent Group'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='group',
            field=models.ManyToManyField(default=None, to='users.UserGroup', blank=True),
        ),
    ]
