# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-14 07:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('sname', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='stu',
            name='clazz',
        ),
        migrations.DeleteModel(
            name='Clazz',
        ),
        migrations.DeleteModel(
            name='Stu',
        ),
    ]
