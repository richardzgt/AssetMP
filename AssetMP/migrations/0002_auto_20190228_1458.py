# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AssetMP', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=60)),
                ('describe', models.CharField(max_length=60, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
        ),
        migrations.AlterField(
            model_name='asset',
            name='machine_type',
            field=models.IntegerField(verbose_name='\u8bbe\u5907\u7c7b\u578b', choices=[(0, '\u9632\u706b\u5899'), (1, '\u8def\u7531\u5668'), (2, '\u7269\u7406\u673a'), (3, '\u4ea4\u6362\u673a')]),
        ),
        migrations.DeleteModel(
            name='MachineType',
        ),
        migrations.AddField(
            model_name='asset',
            name='usage',
            field=models.ForeignKey(verbose_name='\u4e3b\u673a\u4f7f\u7528\u7c7b\u578b', blank=True, to='AssetMP.Usage', null=True),
        ),
    ]
