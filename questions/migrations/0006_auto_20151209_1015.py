# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('saas', '0001_initial'),
        ('questions', '0005_auto_20151208_1752'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='saas.Customer', null=True, verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='quiz',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='saas.Customer', null=True, verbose_name='Customer'),
        ),
        migrations.AddField(
            model_name='sitting',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='saas.Customer', null=True, verbose_name='Customer'),
        ),
        migrations.AlterField(
            model_name='question',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Category', blank=True, to='questions.Category', null=True),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Category', blank=True, to='questions.Category', null=True),
        ),
    ]
