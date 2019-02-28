# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AssetMP', '0003_auto_20190228_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='asset',
            name='uhight',
            field=models.IntegerField(default=0, verbose_name='u\u9ad8', choices=[(0, 1), (1, 2), (2, 4)]),
        ),
    ]
