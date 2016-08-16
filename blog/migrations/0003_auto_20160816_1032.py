# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160622_1848'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(verbose_name='link名字', max_length=20)),
                ('href_name', models.CharField(verbose_name='链接', max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='article',
            name='abstract',
            field=models.TextField(help_text='可选，如若为空将摘取正文的前54个字符', verbose_name='摘要', max_length=500, blank=True, null=True),
        ),
    ]
