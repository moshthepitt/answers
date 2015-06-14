# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('answers', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
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
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='User'),
        ),
        migrations.AddField(
            model_name='multiplechoiceanswer',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Answer', to='questions.MultipleChoiceOption'),
        ),
    ]
