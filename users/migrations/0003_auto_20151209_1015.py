# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0001_initial'),
        ('users', '0002_auto_20150708_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='usergroup',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='saas.Customer', null=True, verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='saas.Customer', null=True, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='users.UserProfile', null=True, verbose_name='Group Manager'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='users.UserGroup', null=True, verbose_name='Parent Group'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='manager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, to='users.UserProfile', blank=True, help_text="Select this user's manager", null=True, verbose_name='Manager'),
        ),
    ]
