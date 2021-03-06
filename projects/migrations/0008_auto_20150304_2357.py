# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20150304_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='preview',
            field=models.ImageField(blank=True, verbose_name='Project Preview', null=True, upload_to='images'),
            preserve_default=True,
        ),
    ]
