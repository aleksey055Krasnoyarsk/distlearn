# Generated by Django 3.1.7 on 2021-03-20 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Домашнее задание', 'verbose_name_plural': 'Домашние задания'},
        ),
    ]
