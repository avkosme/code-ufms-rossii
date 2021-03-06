# Generated by Django 2.0.7 on 2018-08-08 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='d6162070130',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guid', models.CharField(max_length=500)),
                ('fio', models.CharField(max_length=500)),
                ('born_date', models.CharField(max_length=500)),
                ('born_place', models.CharField(default=False, max_length=500)),
                ('pass_num', models.CharField(max_length=500)),
                ('pass_date', models.CharField(max_length=500)),
                ('pass_issued', models.CharField(max_length=500)),
                ('code', models.CharField(max_length=500)),
                ('inn', models.CharField(max_length=500)),
                ('name', models.CharField(max_length=500)),
                ('number', models.CharField(max_length=500)),
            ],
        ),
        migrations.RenameField(
            model_name='d4826085213',
            old_name='born',
            new_name='born_date',
        ),
        migrations.AddField(
            model_name='d4826085213',
            name='born_place',
            field=models.CharField(default=False, max_length=500),
        ),
    ]
