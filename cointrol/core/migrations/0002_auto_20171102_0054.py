# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 23:54
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(blank=True, help_text='Bitstamp login number', max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('open', 'open'), ('cancelled', 'cancelled'), ('processed', 'processed')], db_index=True, default=None, max_length=255),
        ),
        migrations.AlterField(
            model_name='order',
            name='type',
            field=models.IntegerField(choices=[(0, 'buy'), (1, 'sell')], db_index=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'deposit'), (1, 'withdrawal'), (2, 'trade')], db_index=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
