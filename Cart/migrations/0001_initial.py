# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-01-14 14:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Market', '0001_initial'),
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AxfCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('c_is_select', models.BooleanField(default=True)),
                ('c_goods_num', models.IntegerField(default=1)),
                ('c_goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Market.AxfGoods')),
                ('c_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='User.AxfUser')),
            ],
            options={
                'db_table': 'axf_cart',
            },
        ),
    ]
