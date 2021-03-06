# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
            ],
            options={
                'verbose_name': 'Answer',
                'verbose_name_plural': 'Answers',
            },
        ),
        migrations.CreateModel(
            name='BooleanAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='answers.Answer')),
                ('answer', models.BooleanField(verbose_name='Answer')),
            ],
            options={
                'verbose_name': 'Boolean Answer',
                'verbose_name_plural': 'Boolean Answers',
            },
            bases=('answers.answer',),
        ),
        migrations.CreateModel(
            name='EssayAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='answers.Answer')),
                ('answer', models.TextField(verbose_name='Answer')),
            ],
            options={
                'verbose_name': 'Essay Answer',
                'verbose_name_plural': 'Essay Answers',
            },
            bases=('answers.answer',),
        ),
        migrations.CreateModel(
            name='MultipleChoiceAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='answers.Answer')),
            ],
            options={
                'verbose_name': 'Multiple Choice Answer',
                'verbose_name_plural': 'Multiple Choice Answers',
            },
            bases=('answers.answer',),
        ),
        migrations.CreateModel(
            name='RatingAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='answers.Answer')),
                ('answer', models.PositiveIntegerField(verbose_name='Answer', choices=[(1, 'Strongly Disagree'), (2, 'Disagree'), (3, 'Neither Agree Nor Disagree'), (4, 'Agree'), (5, 'Strongly Agree')])),
            ],
            options={
                'verbose_name': 'Rating Answer',
                'verbose_name_plural': 'Rating Answers',
            },
            bases=('answers.answer',),
        ),
        migrations.CreateModel(
            name='TextAnswer',
            fields=[
                ('answer_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='answers.Answer')),
                ('answer', models.CharField(max_length=255, verbose_name='Answer')),
            ],
            options={
                'verbose_name': 'Text Answer',
                'verbose_name_plural': 'Text Answers',
            },
            bases=('answers.answer',),
        ),
        migrations.AddField(
            model_name='answer',
            name='polymorphic_ctype',
            field=models.ForeignKey(related_name='polymorphic_answers.answer_set+', editable=False, to='contenttypes.ContentType', null=True),
        ),
    ]
