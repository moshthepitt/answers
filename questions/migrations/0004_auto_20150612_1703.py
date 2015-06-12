# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20150612_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleChoiceOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('title', models.CharField(help_text='Input the answer as you want it displayed', max_length=300, verbose_name='Answer')),
                ('correct_answer', models.BooleanField(default=False, help_text='Is this a correct answer?', verbose_name='Correct Answer')),
                ('question', models.ForeignKey(verbose_name='Question', to='questions.MultipleChoiceQuestion')),
            ],
            options={
                'verbose_name': 'Multiple Choice Answer',
                'verbose_name_plural': 'Multiple Choice Answers',
            },
        ),
        migrations.RemoveField(
            model_name='multiplechoiceanswer',
            name='question',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['order'], 'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.DeleteModel(
            name='MultipleChoiceAnswer',
        ),
    ]
