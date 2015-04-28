# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('address_one', models.CharField(max_length=256)),
                ('address_two', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=64)),
                ('region', models.CharField(max_length=64)),
                ('country', models.CharField(max_length=64)),
                ('contact_phone_number', models.CharField(max_length=15)),
                ('san', models.CharField(max_length=20, null=True)),
                ('stripe_key', models.CharField(verbose_name='stripe key', max_length=40, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('stripe_id', models.CharField(max_length=40)),
                ('display_name', models.CharField(max_length=24)),
                ('price', models.FloatField()),
                ('slug', models.CharField(max_length=24)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('plan', models.ForeignKey(related_name='users', to='web.Plan')),
                ('user', models.ForeignKey(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='company',
            name='plan',
            field=models.ForeignKey(related_name='companies', to='web.Plan'),
        ),
    ]
