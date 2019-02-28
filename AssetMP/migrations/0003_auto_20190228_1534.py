# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AssetMP', '0002_auto_20190228_1458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='asset',
            name='uhight',
        ),
        migrations.AlterField(
            model_name='asset',
            name='machine_type',
            field=models.IntegerField(verbose_name='\u8bbe\u5907\u7c7b\u578b', choices=[(0, '\u9632\u706b\u5899'), (1, '\u8def\u7531\u5668'), (2, '\u4ea4\u6362\u673a'), (3, '\u7269\u7406\u673a')]),
        ),
    ]
