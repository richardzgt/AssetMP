# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AssetMP', '0004_asset_uhight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, verbose_name='\u673a\u623f', to='AssetMP.IDC'),
        ),
    ]
