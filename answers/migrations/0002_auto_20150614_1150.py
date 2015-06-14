# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reviews', '0001_initial'),
        ('answers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='peer_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to='reviews.PeerReview', null=True, verbose_name='Peer Review'),
        ),
        migrations.AddField(
            model_name='answer',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, default=None, blank=True, to=settings.AUTH_USER_MODEL, null=True, verbose_name='User'),
        ),
    ]
