# Generated by Django 3.1.4 on 2021-01-09 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0005_groups_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groups',
            name='slug',
        ),
    ]
