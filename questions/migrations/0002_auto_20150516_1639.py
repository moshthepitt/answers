# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('questions', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='essayquestion',
            options={'verbose_name': 'Essay Question', 'verbose_name_plural': 'Essay Questions'},
        ),
        migrations.AddField(
            model_name='question',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_questions.question_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='required',
            field=models.BooleanField(default=True, help_text='Is this question required?', verbose_name='Required'),
        ),
    ]
