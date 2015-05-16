# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import core.utils
import mptt.fields
import django.db.models.deletion
import django.core.validators
import autoslug.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('title', models.CharField(help_text='The category title as you want it displayed', max_length=300, verbose_name='Category Title')),
                ('description', models.TextField(help_text='A more detailed description of the category', verbose_name='Description', blank=True)),
                ('active', models.BooleanField(default=True, verbose_name='Active')),
                ('order', models.PositiveIntegerField()),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='questions.Category', null=True, verbose_name='Parent Category')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='MultipleChoiceAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('title', models.CharField(help_text='INput the answer as you want it displayed', max_length=300, verbose_name='Answer')),
                ('correct_answer', models.BooleanField(default=False, help_text='Is this a correct answer?', verbose_name='Correct Answer')),
            ],
            options={
                'verbose_name': 'Multiple Choice Answer',
                'verbose_name_plural': 'Multiple Choice Answers',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('title', models.CharField(help_text='The question as you want it displayed', max_length=300, verbose_name='Question')),
                ('description', models.TextField(help_text='A more detailed description of the question', verbose_name='Description', blank=True)),
                ('image', models.ImageField(default=None, upload_to=core.utils.PathAndRename(b'questions/'), null=True, verbose_name='Image', blank=True)),
                ('required', models.BooleanField(default=True, help_text='Is this question required?', verbose_name='Rquired')),
                ('explanation', models.TextField(help_text='Explanation to be shown after the question has been answered', verbose_name='Explanation', blank=True)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, verbose_name='Created on')),
                ('updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated on')),
                ('title', models.CharField(max_length=300, verbose_name='Title')),
                ('slug', autoslug.fields.AutoSlugField(unique=True, max_length=255)),
                ('description', models.TextField(help_text='A more detailed description of the quiz', verbose_name='Description', blank=True)),
                ('question_ordering', models.CharField(default=b'2', help_text='How should the questions in this quix be ordered?', max_length=1, verbose_name='Question Ordering', choices=[(b'1', 'Date'), (b'2', 'Alphabetical'), (b'3', 'Random')])),
                ('max_questions', models.PositiveIntegerField(default=None, help_text='Number of questions to be answered on each attempt.', null=True, verbose_name='Max Questions', blank=True)),
                ('answers_after_question', models.BooleanField(default=False, help_text='Show answers after each question?', verbose_name='Answers after question')),
                ('answers_at_end', models.BooleanField(default=False, help_text='Show answers at the end of the whole quiz?', verbose_name='Answers at end')),
                ('single_attempt', models.BooleanField(default=False, help_text='If yes, only one attempt by a user will be permitted. Non users cannot sit this exam.', verbose_name='Single Attempt')),
                ('pass_mark', models.SmallIntegerField(default=0, help_text='Percentage required to pass exam.', blank=True, validators=[django.core.validators.MaxValueValidator(100)])),
                ('success_text', models.TextField(help_text='Displayed if user passes.', verbose_name='Success Text', blank=True)),
                ('fail_text', models.TextField(help_text='Displayed if user fails.', verbose_name='Fail Text', blank=True)),
                ('draft', models.BooleanField(default=False, help_text='If yes, the quiz is not displayed in the quiz list and can only be taken by users who can edit quizzes.', verbose_name='Draft')),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, to='questions.Category', null=True)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='BooleanQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='questions.Question')),
                ('true_label', models.CharField(default='True', help_text='What will represent the True/Yes option', max_length=50, verbose_name='True Label')),
                ('false_label', models.CharField(default='False', help_text='What will represent the False/No option', max_length=50, verbose_name='False Label')),
                ('correct_answer', models.NullBooleanField(default=None, help_text='Which is the correct answer to this question?', verbose_name='Correct Answer')),
            ],
            options={
                'verbose_name': 'Boolean Question',
                'verbose_name_plural': 'Boolean Questions',
            },
            bases=('questions.question',),
        ),
        migrations.CreateModel(
            name='EssayQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='questions.Question')),
            ],
            options={
                'verbose_name': 'Text Question',
                'verbose_name_plural': 'Text Questions',
            },
            bases=('questions.question',),
        ),
        migrations.CreateModel(
            name='MultipleChoiceQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='questions.Question')),
            ],
            options={
                'verbose_name': 'Multiple Choice Question',
                'verbose_name_plural': 'Multiple Choice Questions',
            },
            bases=('questions.question',),
        ),
        migrations.CreateModel(
            name='RatingQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='questions.Question')),
            ],
            options={
                'verbose_name': 'Rating Question',
                'verbose_name_plural': 'Rating Questions',
            },
            bases=('questions.question',),
        ),
        migrations.CreateModel(
            name='TextQuestion',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='questions.Question')),
            ],
            options={
                'verbose_name': 'Text Question',
                'verbose_name_plural': 'Text Questions',
            },
            bases=('questions.question',),
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(verbose_name='Category', blank=True, to='questions.Category', null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(to='questions.Quiz', verbose_name='Quiz', blank=True),
        ),
        migrations.AddField(
            model_name='multiplechoiceanswer',
            name='question',
            field=models.ForeignKey(verbose_name='Question', to='questions.MultipleChoiceQuestion'),
        ),
    ]
