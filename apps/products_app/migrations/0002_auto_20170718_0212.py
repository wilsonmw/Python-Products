# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-18 02:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cost',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='product',
            name='weight',
            field=models.IntegerField(default=0),
        ),
    ]