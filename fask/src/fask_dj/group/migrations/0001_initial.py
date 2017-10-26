# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-26 23:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(help_text='The short description for that element', max_length=200, verbose_name='Description')),
                ('annotation', models.TextField(blank=True, help_text='Here you can give more deep information', verbose_name='Annotation')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
