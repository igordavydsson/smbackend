# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-24 14:50
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('observations', '0002_change_org_to_dept'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='observableproperty',
            name='services',
        ),
    ]