# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 00:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_review', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='author',
        ),
        migrations.AddField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(null=True, related_name='authors', to='belt_review.Book'),
        ),
    ]
