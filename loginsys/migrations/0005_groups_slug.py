# Generated by Django 3.1.4 on 2021-01-08 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loginsys', '0004_auto_20210101_0816'),
    ]

    operations = [
        migrations.AddField(
            model_name='groups',
            name='slug',
            field=models.SlugField(blank=True, default='', max_length=150),
        ),
    ]
