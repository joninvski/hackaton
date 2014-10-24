# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='company',
            options={'verbose_name_plural': 'Companies'},
        ),
        migrations.AlterModelOptions(
            name='data',
            options={'verbose_name_plural': 'Data'},
        ),
        migrations.AddField(
            model_name='data',
            name='data_type',
            field=models.IntegerField(default=1, choices=[(1, b'INCOMING'), (2, b'OUTGOING')]),
            preserve_default=False,
        ),
    ]
