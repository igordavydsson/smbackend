# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-07 16:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0033_translate_call_charge_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unit',
            name='organizer_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'ASSOCIATION'), (1, 'FOUNDATION'), (2, 'GOVERNMENT'), (3, 'GOVERNMENTAL_COMPANY'), (4, 'JOINT_MUNICIPAL_AUTHORITY'), (5, 'MUNICIPAL_ENTERPRISE_GROUP'), (6, 'MUNICIPALITY'), (7, 'MUNICIPALLY_OWNED_COMPANY'), (8, 'ORGANIZATION'), (9, 'OTHER_REGIONAL_COOPERATION_ORGANIZATION'), (10, 'PRIVATE_ENTERPRISE'), (11, 'UNKNOWN')], null=True),
        ),
    ]