# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 01:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_review', '0003_auto_20170603_1813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='book',
            field=models.ManyToManyField(null=True, related_name='authors', to='belt_review.Book'),
        ),
    ]
