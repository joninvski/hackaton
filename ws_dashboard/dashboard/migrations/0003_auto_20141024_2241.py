# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20141024_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='volume',
            field=models.IntegerField(help_text=b'Amount of kb exchanged'),
            preserve_default=True,
        ),
    ]
