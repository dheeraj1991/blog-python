# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100, verbose_name=b'Title')),
                ('author', models.CharField(max_length=25, verbose_name=b'Author')),
                ('publication_date', models.DateField(verbose_name=b'Publication Date')),
                ('hero_image', models.ImageField(default=datetime.date.today, upload_to=b'', verbose_name=b'Hero Image')),
                ('optional_image', models.ImageField(upload_to=b'', null=True, verbose_name=b'Alternate Image')),
                ('content', models.TextField(verbose_name=b'Content')),
            ],
            options={
                'db_table': 'blog_article',
            },
        ),
    ]
