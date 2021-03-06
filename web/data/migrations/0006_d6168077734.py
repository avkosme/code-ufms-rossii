# Generated by Django 2.0.7 on 2018-08-08 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_auto_20180808_0725'),
    ]

    operations = [
        migrations.CreateModel(
            name='d6168077734',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(max_length=500)),
                ('fio', models.CharField(max_length=500)),
                ('born_date', models.CharField(max_length=500)),
                ('born_place', models.CharField(blank=True, default='', max_length=500)),
                ('pass_num', models.CharField(max_length=500)),
                ('pass_date', models.CharField(max_length=500)),
                ('pass_issued', models.CharField(max_length=500)),
                ('code', models.CharField(max_length=500)),
                ('inn', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('number', models.CharField(max_length=500)),
            ],
        ),
    ]
