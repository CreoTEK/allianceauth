# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-02 10:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seatuser',
            options={'permissions': (('access_seat', 'Can access the SeAT service'),)},
        ),
    ]
