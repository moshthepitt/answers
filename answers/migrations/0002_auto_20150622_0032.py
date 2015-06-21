# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
        ('users', '0001_initial'),
        ('questions', '0001_initial'),
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Question', to='questions.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='reviews.Review', null=True, verbose_name='Review'),
        ),
        migrations.AddField(
            model_name='answer',
            name='userprofile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='users.UserProfile', null=True, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='multiplechoiceanswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Answer', to='questions.MultipleChoiceOption'),
        ),
    ]
