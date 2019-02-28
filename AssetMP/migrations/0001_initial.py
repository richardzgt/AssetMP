# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=50, null=True, blank=True)),
                ('ipadd', models.CharField(max_length=20, null=True, blank=True)),
                ('manager_ip', models.CharField(max_length=20, null=True, verbose_name='\u7ba1\u7406\u7f51ip', blank=True)),
                ('remote_card_ip', models.CharField(max_length=20, null=True, verbose_name='\u8fdc\u63a7\u5361ip', blank=True)),
                ('product_name', models.CharField(max_length=20, verbose_name='\u8bbe\u5907\u578b\u53f7')),
                ('serial_number', models.CharField(unique=True, max_length=20, verbose_name='\u5e8f\u5217\u53f7')),
                ('suppliers', models.CharField(max_length=32, null=True, verbose_name='\u4f9b\u5e94\u5546', blank=True)),
                ('purchase_at', models.DateField(auto_now=True, verbose_name='\u8d2d\u4e70\u65f6\u95f4')),
                ('department', models.CharField(max_length=20, null=True, verbose_name='\u4f7f\u7528\u90e8\u95e8', blank=True)),
                ('sign_time', models.DateField(null=True, verbose_name='\u7ef4\u4fdd\u7b7e\u7ea6\u65f6\u95f4', blank=True)),
                ('expire_time', models.DateField(null=True, verbose_name='\u7ef4\u4fdd\u8fc7\u671f\u65f6\u95f4', blank=True)),
                ('cpu', models.CharField(max_length=60, null=True, blank=True)),
                ('disk', models.CharField(max_length=60, null=True, blank=True)),
                ('memory', models.CharField(max_length=60, null=True, blank=True)),
                ('system_version', models.CharField(max_length=80, null=True, verbose_name='\u64cd\u4f5c\u7cfb\u7edf', blank=True)),
                ('cabinet', models.CharField(max_length=32, verbose_name='\u673a\u67dc\u53f7')),
                ('uhight', models.IntegerField(verbose_name='u\u9ad8')),
                ('railnum', models.IntegerField(verbose_name='\u5bfc\u8f68\u4f4d\u7f6e')),
                ('number', models.CharField(max_length=32, null=True, verbose_name='\u8d44\u4ea7\u7f16\u53f7', blank=True)),
                ('describe', models.CharField(max_length=60, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u8bbe\u5907\u4fe1\u606f\u8868',
                'verbose_name_plural': '\u8bbe\u5907\u4fe1\u606f\u8868',
            },
        ),
        migrations.CreateModel(
            name='AssetRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=30, null=True)),
                ('alert_time', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField(null=True, blank=True)),
                ('comment', models.TextField(null=True, blank=True)),
                ('asset', models.ForeignKey(to='AssetMP.Asset')),
            ],
        ),
        migrations.CreateModel(
            name='AssetStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('detail', models.CharField(max_length=32, null=True, blank=True)),
                ('describe', models.CharField(max_length=60, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u8bbe\u5907\u72b6\u6001',
                'verbose_name_plural': '\u8bbe\u5907\u72b6\u6001',
            },
        ),
        migrations.CreateModel(
            name='Belong',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u516c\u53f8\u540d\u79f0')),
                ('nickname', models.CharField(max_length=32, verbose_name='\u5e73\u53f0\u7b80\u79f0')),
                ('describe', models.CharField(max_length=60, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u6240\u5c5e\u516c\u53f8',
                'verbose_name_plural': '\u6240\u5c5e\u516c\u53f8',
            },
        ),
        migrations.CreateModel(
            name='IDC',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u673a\u623f\u540d\u79f0')),
                ('bandwidth', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u673a\u623f\u5e26\u5bbd', blank=True)),
                ('linkman', models.CharField(default=b'', max_length=16, null=True, verbose_name='\u8054\u7cfb\u4eba', blank=True)),
                ('phone', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u8054\u7cfb\u7535\u8bdd', blank=True)),
                ('address', models.CharField(default=b'', max_length=128, null=True, verbose_name='\u673a\u623f\u5730\u5740', blank=True)),
                ('network', models.TextField(default=b'', null=True, verbose_name='IP\u5730\u5740\u6bb5', blank=True)),
                ('date_added', models.DateField(auto_now=True, null=True)),
                ('operator', models.CharField(default=b'', max_length=32, null=True, verbose_name='\u8fd0\u8425\u5546', blank=True)),
                ('comment', models.CharField(default=b'', max_length=128, null=True, verbose_name='\u5907\u6ce8', blank=True)),
                ('needed_cabinet', models.BooleanField(default=True, verbose_name='\u662f\u5426\u9700\u8981\u6e32\u67d3\u673a\u67b6\u56fe')),
            ],
            options={
                'verbose_name': 'IDC\u673a\u623f',
                'verbose_name_plural': 'IDC\u673a\u623f',
            },
        ),
        migrations.CreateModel(
            name='MachineType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('detail', models.CharField(max_length=32, null=True, blank=True)),
                ('uhigh', models.IntegerField(verbose_name='\u8bbe\u5907\u7684u\u9ad8\u5ea6', choices=[(0, 1), (0, 2), (0, 4)])),
                ('describe', models.CharField(max_length=60, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u4e3b\u673a\u4f7f\u7528\u7c7b\u578b',
                'verbose_name_plural': '\u4e3b\u673a\u4f7f\u7528\u7c7b\u578b',
            },
        ),
        migrations.CreateModel(
            name='ManType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('detail', models.CharField(max_length=32, null=True, blank=True)),
                ('describe', models.CharField(max_length=60, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u5382\u5bb6\u4fe1\u606f',
                'verbose_name_plural': '\u5382\u5bb6\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u5e73\u53f0\u540d\u79f0')),
                ('nickname', models.CharField(max_length=32, verbose_name='\u5e73\u53f0\u7b80\u79f0')),
                ('describe', models.CharField(max_length=60, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u5e73\u53f0\u4fe1\u606f',
                'verbose_name_plural': '\u5e73\u53f0\u4fe1\u606f',
            },
        ),
        migrations.CreateModel(
            name='SignDep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32, verbose_name='\u7ef4\u4fdd\u516c\u53f8\u540d\u79f0')),
                ('contact', models.CharField(max_length=32, verbose_name='\u8054\u7cfb\u4eba')),
                ('phone', models.CharField(max_length=32, verbose_name='\u8054\u7cfb\u65b9\u5f0f')),
                ('describe', models.CharField(max_length=60, null=True, verbose_name='\u5907\u6ce8', blank=True)),
            ],
            options={
                'verbose_name': '\u7ef4\u4fdd\u5355\u4f4d',
                'verbose_name_plural': '\u7ef4\u4fdd\u5355\u4f4d',
            },
        ),
        migrations.AddField(
            model_name='asset',
            name='belong',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u6240\u5c5e\u516c\u53f8', blank=True, to='AssetMP.Belong', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u673a\u623f', blank=True, to='AssetMP.IDC', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='machine_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, verbose_name='\u8bbe\u5907\u7c7b\u578b', to='AssetMP.MachineType'),
        ),
        migrations.AddField(
            model_name='asset',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u5382\u5bb6', blank=True, to='AssetMP.ManType', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='platform',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u5e73\u53f0\u540d\u79f0', blank=True, to='AssetMP.Platform', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='sign_dep',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u7ef4\u4fdd\u5355\u4f4d', blank=True, to='AssetMP.SignDep', null=True),
        ),
        migrations.AddField(
            model_name='asset',
            name='status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='\u673a\u5668\u72b6\u6001', blank=True, to='AssetMP.AssetStatus', null=True),
        ),
    ]
