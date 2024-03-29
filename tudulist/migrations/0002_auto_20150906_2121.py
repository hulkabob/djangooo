# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tudulist', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='whois',
            field=models.CharField(max_length=256, verbose_name='Квестодавець', blank=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='done',
            field=models.BooleanField(verbose_name='Здано'),
        ),
    ]
