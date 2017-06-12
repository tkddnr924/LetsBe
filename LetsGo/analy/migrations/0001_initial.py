# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-06-12 11:49
from __future__ import unicode_literals

import analy.fields
import analy.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=50, verbose_name='Manufacturer')),
                ('camera_model', models.CharField(max_length=50, verbose_name='Model')),
                ('date_time', models.CharField(max_length=50, verbose_name='Date Time')),
                ('iso_speed', models.CharField(max_length=50, verbose_name='ISO Speed')),
                ('color', models.CharField(max_length=50, verbose_name='Color Space')),
                ('latitude', models.CharField(max_length=50, verbose_name='Latitude')),
                ('longitude', models.CharField(max_length=50, verbose_name='Longitude')),
                ('orientation', models.CharField(max_length=50, verbose_name='Direction of Rotation')),
                ('focal_length', models.CharField(max_length=50, verbose_name='Focus Length')),
                ('flash', models.CharField(max_length=50, verbose_name='Flash')),
            ],
            options={
                'db_table': 'Exif_info',
                'ordering': ('-date_time',),
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('image', analy.fields.MyImageField(upload_to=analy.models.Photo.file_path)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Nick Name')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='photo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analy.User'),
        ),
        migrations.AddField(
            model_name='exif',
            name='photo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analy.Photo'),
        ),
    ]
