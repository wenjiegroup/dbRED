# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2020-08-18 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RnaSearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chimpanzee_rnaedit',
            name='Cellline',
            field=models.CharField(max_length=30, verbose_name='Cellline'),
        ),
        migrations.AlterField(
            model_name='rhesus_rnaedit',
            name='Cellline',
            field=models.CharField(max_length=30, verbose_name='Cellline'),
        ),
    ]
