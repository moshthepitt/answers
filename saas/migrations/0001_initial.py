# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('name', models.CharField(max_length=255, verbose_name='Customer name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email address', blank=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=255, verbose_name='Phone Number', blank=True)),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this customer should be treated as active.', verbose_name='Active')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]
