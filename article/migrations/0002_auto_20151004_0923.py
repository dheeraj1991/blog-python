# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='optional_image',
            field=models.ImageField(default='', upload_to=b'', verbose_name=b'Alternate Image', blank=True),
            preserve_default=False,
        ),
    ]
