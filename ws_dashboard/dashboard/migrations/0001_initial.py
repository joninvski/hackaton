# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Call',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caller', models.CharField(max_length=30)),
                ('receiver', models.CharField(max_length=30)),
                ('start_time', models.DateTimeField()),
                ('length', models.IntegerField()),
                ('call_type', models.IntegerField(choices=[(1, b'INCOMING'), (2, b'OUTGOING')])),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lng', models.FloatField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=30)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('volume', models.FloatField(help_text=b'Amount of kb exchanged')),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lng', models.FloatField(null=True, blank=True)),
                ('start_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('role', models.IntegerField(choices=[(1, b'BOSS'), (2, b'SUPERBOSS')])),
                ('phone_number', models.CharField(max_length=30)),
                ('company', models.ForeignKey(related_name='employees_company', to='dashboard.Company')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender', models.CharField(max_length=30)),
                ('receiver', models.CharField(max_length=30)),
                ('sent_time', models.DateTimeField()),
                ('message_type', models.IntegerField(choices=[(1, b'INCOMING'), (2, b'OUTGOING')])),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lng', models.FloatField(null=True, blank=True)),
                ('owner', models.ForeignKey(related_name='messages_employee', to='dashboard.Employee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='data',
            name='owner',
            field=models.ForeignKey(related_name='data_employee', to='dashboard.Employee'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='call',
            name='owner',
            field=models.ForeignKey(related_name='calls_employee', to='dashboard.Employee'),
            preserve_default=True,
        ),
    ]
