# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MUSIC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_name', models.CharField(max_length=200)),
                ('singer', models.CharField(max_length=200)),
                ('frequency', models.CharField(max_length=200)),
                ('mis_id', models.CharField(max_length=200)),
                ('star_id', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'music_web_music',
                'managed': False,
            },
        ),
    ]
